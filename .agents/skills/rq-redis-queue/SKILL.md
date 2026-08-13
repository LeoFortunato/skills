---
name: rq-redis-queue
description: Implement and review RQ (Redis Queue) background jobs, queues, workers, retries, scheduling, timeouts, registries, heartbeats, cancellation, and graceful shutdown. Use when a Python service enqueues or executes asynchronous work with RQ.
metadata:
  author: Leonardo Fortunato
  license: MIT
  source: https://github.com/yonatangross/orchestkit
---

# RQ Async Jobs

Use this skill for RQ workflows only. Keep RQ as the queue and worker technology in scope; do
not introduce or compare another task framework unless the user explicitly asks for a
comparison.

## Workflow

Follow this sequence when implementing or reviewing RQ behavior:

1. Inspect the repository's pinned `rq` and `redis` versions, existing queue names, worker entry
   points, job metadata contract, and tests before proposing a change.
2. Keep HTTP handlers and producers non-blocking: validate the request, enqueue an importable
   function with small serializable arguments, and return the stable job ID.
3. Choose explicit queue, connection, serializer, timeout, queued-job TTL, result TTL, and
   failure TTL settings. Keep `ttl`, `job_timeout`, `result_ttl`, and `failure_ttl` distinct.
4. Make retries safe: classify transient failures, configure `Retry`, and make the job
   idempotent using a stable job ID or an application-level idempotency key.
5. Choose the worker model deliberately. Use a normal `Worker` for standard process-isolated RQ
   execution. Use `SimpleWorker` in tests or in a custom async consumer only when the consumer
   owns heartbeat, lifecycle, cleanup, and concurrency responsibilities explicitly.
6. Design shutdown and recovery before adding concurrency: stop dequeuing, drain active work,
   finalize RQ state, cancel heartbeat tasks, and register worker death in a `finally` path.
7. Verify status and recovery through RQ jobs, executions, registries, results, queue depth, and
   worker heartbeats. Keep large outputs outside Redis and retain only references in job data.

## Scope boundary

This skill covers:

- `Redis`, `Queue`, `Job`, `Worker`, `SimpleWorker`, and RQ worker classes.
- Enqueueing, importable job functions, JSON serialization, job IDs, dependencies, and queue
  selection.
- Timeouts, queued-job/result/failure TTLs, retries, scheduled jobs, cancellation, termination,
  registries, results, monitoring, testing, and graceful shutdown.
- Custom asyncio consumers that preserve RQ job lifecycle and registry semantics.

Do not preserve unrelated queue-framework sections in this skill. Keep framework-specific details
out of `SKILL.md` and its references.

## Quick start

```python
import os

from redis import Redis
from rq import Queue, Retry
from rq.worker import Worker


connection = Redis.from_url(os.environ["REDIS_URL"])
queue = Queue(
    "default",
    connection=connection,
    serializer="json",
    default_timeout=300,
)

job = queue.enqueue(
    "my_app.jobs.process_payment",
    order_id,
    job_timeout=300,
    result_ttl=86_400,
    failure_ttl=86_400,
    retry=Retry(max=3, interval=[60, 120, 300]),
)

print(job.id)


if __name__ == "__main__":
    Worker([queue], connection=connection, serializer="json").work(
        with_scheduler=True,
    )
```

Run a programmatic worker with `with_scheduler=True` only when scheduled jobs or delayed retry
intervals are required, and protect the worker entry point with `if __name__ == "__main__"`.

## Repository contract

Treat the repository's dependency files and runtime code as authoritative. In this checkout,
the pinned baseline is Python 3.11+, `rq==2.10.0`, and Redis 7.x. Do not use an RQ API introduced
after the pinned version without changing the dependency and its tests together.

Keep request-scoped credentials out of persisted job arguments whenever possible. If a job must
receive a short-lived credential, use the existing repository scrub/finalization path and never
write the credential to descriptions, metadata, results, logs, or public errors.

## Supporting references

Read [references/rq-guidance.md](references/rq-guidance.md) for the RQ-specific operational
delta, version-sensitive decisions, and upstream links.

Read [references/quick-start-examples.md](references/quick-start-examples.md) for standard,
custom-async-consumer, lifecycle, status, and test examples.

Read [references/anti-patterns.md](references/anti-patterns.md) before changing retry,
serialization, shutdown, or result-storage behavior.

Read [references/capability-details.md](references/capability-details.md) when matching a user
request to the RQ capability covered by this skill.

## Validation

Before reporting an RQ change as complete:

- Check that queue and worker serializers match and that every serialized argument is supported
  by the chosen serializer.
- Check that the job function is importable by the worker and does not depend on request-local
  state.
- Check that retry paths are idempotent and that delayed retries have a scheduler.
- Check that cancellation, stop, timeout, failure, and abandoned-job paths remain distinguishable.
- Check that graceful shutdown stops new dequeues before awaiting active jobs.
- Run the smallest relevant unit tests, then the repository's Redis/integration tests when the
  change affects real RQ lifecycle behavior.
- Report skipped runtime checks and distinguish static evidence from a live Redis result.
