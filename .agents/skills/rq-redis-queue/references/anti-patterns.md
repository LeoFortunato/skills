# RQ Anti-Patterns

Avoid these failure and security patterns when working with RQ.

## Never enqueue non-importable work

```python
def local_task():
    ...

# The worker cannot reliably import a function declared in a request or __main__ scope.
queue.enqueue(local_task)
```

Define jobs in an importable module and pass explicit, small arguments.

## Never use pickle for untrusted Redis data

RQ defaults to pickle. Prefer `serializer="json"` on both `Queue` and `Worker` when arguments
are JSON primitives. If a trusted legacy queue still uses pickle, treat the Redis instance and
all job producers as trusted and do not silently mix serializers.

## Never confuse RQ time limits and TTLs

- `job_timeout` limits execution time.
- `ttl` limits how long a queued job may wait.
- `result_ttl` controls successful result retention.
- `failure_ttl` controls failed-job retention.

Configure each deliberately; changing one does not change the others.

## Never retry non-idempotent work blindly

Retries can execute a job more than once. Use a stable job ID or application-level idempotency
key, and make external side effects safe to repeat before configuring `Retry`.

## Never block a worker on its own result

Do not wait for a queued or dependent job from inside an RQ job when that can exhaust the worker
capacity needed to make progress. Enqueue dependencies explicitly and let the producer or status
endpoint observe them.

## Never store large payloads in Redis

Return a small reference to object storage or a database. Keep `job.meta` and results bounded and
free of credentials.

## Never use forceful termination as the normal shutdown path

Use `SIGTERM`/`SIGINT` and let the worker finish its current job. A second signal or `SIGKILL`
is an emergency path that can abandon active work until registry cleanup recovers it.

## Never dequeue while draining

On custom async consumers, set the shutdown event before awaiting active tasks. Cancel heartbeat
tasks only after the job's RQ state has been finalized.
