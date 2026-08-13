# RQ Guidance

This file contains the repository-specific RQ delta. Use the upstream RQ documentation for
product mechanics and keep these decisions for boundaries, ordering, and safety.

## Version boundary

Inspect `pyproject.toml` before using a version-sensitive API. This repository currently pins
Python 3.11+, `rq==2.10.0`, and `redis>=7.4.0,<8.0.0`. Do not use features introduced after the
pinned RQ version without changing the dependency and tests together.

## Connections and serialization

- Pass an explicit Redis connection to each `Queue`, `Worker`, and fetched `Job`.
- Prefer `serializer="json"` on both producer and worker when all job arguments are JSON
  primitives. JSON does not support arbitrary Python objects.
- RQ's default pickle serializer is unsafe for untrusted Redis/job data. Never mix serializers on
  a queue and never silently migrate an existing queue to JSON without coordinating producers and
  workers.
- Keep the Redis URL and credentials in repository settings. Never hardcode them in a job or
  reference file.

## Enqueue contract

- Define the job function in an importable module; do not enqueue request-local or `__main__`
  functions.
- Pass small, explicit arguments. Resolve request context before enqueueing and do not depend on
  ambient user, request, or process state in the worker.
- Use a stable `job_id` for caller-owned idempotency where the application contract requires it.
  Treat duplicate enqueue attempts as an explicit outcome, not as a second side effect.
- Keep credentials out of job arguments. If a short-lived credential is unavoidable, consume and
  scrub it before finalization and exclude it from descriptions, metadata, results, and logs.
- Configure `job_timeout`, `ttl`, `result_ttl`, and `failure_ttl` independently. RQ's default
  execution timeout is 180 seconds; set a bounded value appropriate to the job.

## Queue and worker selection

- RQ creates named queues when jobs are enqueued. Queue order matters with the default dequeue
  strategy and acts as a priority order.
- Use `--dequeue-strategy round_robin` or `RoundRobinWorker` when strict queue priority can starve
  lower queues. Use `random` only when randomized distribution is intentional.
- A standard RQ worker processes one job at a time. Scale with additional worker processes and
  run them under a process manager in production.
- Use `SimpleWorker` for tests, debugging, or environments without `fork()`. It does not emit
  periodic heartbeats during job execution. In a custom async consumer, use it only as an explicit
  lifecycle adapter and maintain heartbeats, finalization, cleanup, and concurrency yourself.

## Custom async consumer lifecycle

When the service owns asyncio concurrency around RQ:

1. Stop new dequeues when shutdown begins.
2. Dequeue with `Queue.dequeue_any(...)` and handle `DequeueTimeout` as an empty poll.
3. Claim and prepare the RQ job before starting application work.
4. Maintain the RQ heartbeat independently of the application coroutine.
5. Enforce the job execution timeout in the application task as well as the RQ job contract when
   the custom consumer bypasses the normal RQ work horse.
6. Finalize successful or failed RQ state exactly once, including registry movement and sanitized
   failure information.
7. Cancel the heartbeat task after finalization and call `register_death()` in `finally`.
8. Await every active task before returning from shutdown.

Do not copy internal lifecycle calls from another RQ version without checking the installed RQ
source and the repository's integration tests.

## Retries and failures

- Use `Retry(max=..., interval=...)` only for failures that are safe to repeat. Keep intervals
  bounded and make external side effects idempotent.
- Delayed retry intervals require a worker with the scheduler enabled (`--with-scheduler` or
  `work(with_scheduler=True)`).
- Inspect `FailedJobRegistry`, `job.exc_info`, and execution results when diagnosing failures.
- A stopped active job enters `FailedJobRegistry` but is not automatically retried by configured
  `Retry`. `job.cancel()` prevents a queued job from running and places it in
  `CanceledJobRegistry`; it is not an active-job termination command.
- Treat abandoned jobs as a recovery signal, not proof that duplicate execution is impossible.

## Scheduling and registries

- Use `enqueue_at()` for an explicit datetime and `enqueue_in()` for a `timedelta`.
- Scheduled jobs remain in `ScheduledJobRegistry` until the scheduler enqueues them.
- Monitor `StartedJobRegistry`, `FinishedJobRegistry`, `FailedJobRegistry`,
  `DeferredJobRegistry`, `ScheduledJobRegistry`, and `CanceledJobRegistry` according to the
  behavior under review.
- Keep programmatic scheduler startup behind `if __name__ == "__main__"` because RQ's scheduler
  uses a separate process.

## Results and monitoring

- Use `job.get_status(refresh=True)`, `job.get_meta(refresh=True)`, `job.latest_result()`, and
  `job.results()` for status and execution history.
- Use `job.last_heartbeat`, execution heartbeats, `worker.last_heartbeat`, and `Worker.count()`
  for liveness signals. A stale heartbeat signals recovery work; it does not prove that duplicate
  execution is safe.
- Use `rq info` or the RQ dashboard for queue and worker visibility. Queue length counts queued
  jobs and does not include deferred jobs.
- Store large files and payloads outside Redis. Keep job results and `job.meta` small, bounded,
  sanitized, and reference-based.

## Testing

- Use `SimpleWorker` for worker-path tests that should not fork.
- Use `Queue(is_async=False, connection=fake_redis)` for focused synchronous job tests.
- Use an isolated Redis integration test to verify queue order, serializers, TTLs, retries,
  heartbeats, registries, cancellation, and custom consumer shutdown.
- Patch the repository's module-level settings and Redis boundary in tests; do not create a second
  settings object that bypasses the configured runtime.

## Upstream RQ documentation

- [Documentation overview](https://python-rq.org/docs/)
- [Queues and enqueueing](https://python-rq.org/docs/)
- [Workers](https://python-rq.org/docs/workers/)
- [Jobs and lifecycle](https://python-rq.org/docs/jobs/)
- [Results and timeouts](https://python-rq.org/docs/results/)
- [Exceptions and retries](https://python-rq.org/docs/exceptions/)
- [Scheduling](https://python-rq.org/docs/scheduling/)
- [Job registries](https://python-rq.org/docs/job_registries/)
- [Monitoring](https://python-rq.org/docs/monitoring/)
- [Testing](https://python-rq.org/docs/testing/)
