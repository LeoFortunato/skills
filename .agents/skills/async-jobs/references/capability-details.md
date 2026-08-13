# RQ Capability Details

### rq-enqueue
**Keywords:** RQ, Redis Queue, queue, enqueue, job ID, serializer, JSON, TTL, dependency
**Solves:**
- Enqueueing importable Python jobs with explicit Redis connections.
- Choosing queue names, stable IDs, serializers, timeouts, and retention settings.
- Preserving idempotency and request/worker boundaries.

### rq-worker
**Keywords:** RQ worker, Worker, SimpleWorker, queue order, dequeue strategy, process isolation
**Solves:**
- Running standard RQ workers under a process manager.
- Choosing worker classes and queue dequeue behavior.
- Building a custom async consumer without losing RQ lifecycle semantics.

### rq-lifecycle
**Keywords:** heartbeat, shutdown, SIGTERM, stop job, cancel job, abandoned job, registry
**Solves:**
- Maintaining worker/job heartbeats and detecting stale work.
- Distinguishing queued cancellation from stopping active execution.
- Draining active jobs and registering worker death during graceful shutdown.

### rq-retries
**Keywords:** Retry, retry interval, scheduled job, failure, FailedJobRegistry, idempotency
**Solves:**
- Configuring bounded retries for transient failures.
- Enabling the scheduler for delayed retry intervals.
- Separating retryable failures from permanent failures.

### rq-observability
**Keywords:** job status, result, latest_result, job.meta, rq info, Worker.count, monitoring
**Solves:**
- Reading job status, execution results, metadata, and registries.
- Monitoring queue depth, active workers, and heartbeats.
- Keeping Redis results small and externally storing large outputs.
