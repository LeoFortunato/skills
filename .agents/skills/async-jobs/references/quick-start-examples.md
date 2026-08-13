# RQ Examples

## Standard producer and worker

```python
import os

from redis import Redis
from rq import Queue, Retry
from rq.worker import Worker


connection = Redis.from_url(os.environ["REDIS_URL"])
queue = Queue("default", connection=connection, serializer="json", default_timeout=300)

job = queue.enqueue(
    "my_app.jobs.generate_report",
    report_id,
    job_timeout=300,
    ttl=60,
    result_ttl=86_400,
    failure_ttl=86_400,
    retry=Retry(max=3, interval=[30, 90, 300]),
)

# Return job.id to the caller; do not wait for job completion in the request.
print(job.id)


if __name__ == "__main__":
    Worker([queue], connection=connection, serializer="json").work(
        with_scheduler=True,
    )
```

## Custom asyncio consumer

Use this pattern only when the service intentionally owns concurrent asyncio tasks while using
RQ for job storage, queueing, status, and failure semantics.

```python
import asyncio

from rq import Queue, SimpleWorker
from rq.exceptions import DequeueTimeout
from rq.job import Job


async def maintain_heartbeat(
    worker: SimpleWorker,
    job: Job,
    interval_seconds: float,
) -> None:
    while True:
        await asyncio.sleep(interval_seconds)
        await asyncio.to_thread(worker.maintain_heartbeats, job)


def dequeue_one(queues, connection):
    try:
        return Queue.dequeue_any(queues, timeout=1, connection=connection)
    except DequeueTimeout:
        return None
```

The consumer must stop dequeuing before draining active tasks. For every claimed job, prepare
the RQ lifecycle, start heartbeat maintenance independently, finalize success or failure, cancel
the heartbeat task, and call `register_death()` in a `finally` path. Keep this code aligned with
the installed RQ version because lifecycle methods may be implementation-sensitive.

## Status and results

```python
from rq.job import Job


job = Job.fetch(job_id, connection=connection)
status = job.get_status(refresh=True)
metadata = job.get_meta(refresh=True)
latest = job.latest_result()
if latest is not None:
    print(latest.type, latest.return_value, latest.exc_string)
```

Use `job.return_value()` for the latest successful return value, and use the registries for
started, finished, failed, deferred, scheduled, and canceled work. Do not block a request or a
worker indefinitely while waiting for a result.

## Tests

Use `SimpleWorker` for tests that need RQ worker behavior without `fork()`. For a focused unit
test, `Queue(is_async=False, connection=fake_redis)` runs the job immediately; assert status,
metadata, and result behavior without requiring a worker process.
