# 1. Understanding Your Benchmark Output

| Metric | Your Result | Meaning |
|--------|-------------|---------|
| Total requests | 10 | You submitted 10 inference requests. |
| Successful | 10 | All requests received successful responses. |
| Failed | 0 | No request failed or timed out. |
| Total duration | 46.43 sec | Entire benchmark took 46.43 seconds. |
| Average latency | 9.28 sec | Average time taken by an individual request. |
| p50 latency | 9.19 sec | 50% of requests completed in 9.19 sec or less. |
| p95 latency | 9.59 sec | Approximately 95% completed within 9.59 sec. |
| p99 latency | 9.59 sec | Approximately 99% completed within 9.59 sec, based on this small sample. |
| Total output tokens | 1,500 | Model generated 1,500 tokens across all responses. |
| Aggregate throughput | 32.31 tokens/sec | Overall output tokens divided by total benchmark duration. |
| Average request generation rate | 16.16 tokens/sec | Average of each request's output tokens divided by its individual elapsed time. |

## 2. Understanding Latency

### Configuration

```
TOTAL_REQUESTS = 10
CONCURRENCY = 2
```

This means:
- **Total requests:** 10
- **Maximum simultaneous requests:** 2
- **Batch execution:** The benchmark processes requests in approximately 5 batches of 2.

### Illustrative Request Execution

**Two concurrent requests at a time**

| Batch | Requests |
|-------|----------|
| Batch 1 | Request 1 and 2 |
| Batch 2 | Request 3 and 4 |
| Batch 3 | Request 5 and 6 |
| Batch 4 | Request 7 and 8 |
| Batch 5 | Request 9 and 10 |

> **Note:** Conceptual illustration, not actual measured request timings.

### Key Takeaway

Your average latency is **9.28 seconds**. This is the average elapsed time per request, not the total time for all 10 requests.
## 3. Understanding Aggregate Throughput vs. Generation Rate

This is particularly important for LLM benchmarking.

### Aggregate Throughput: 32.31 tokens/sec

**Calculation:**

$$\text{Throughput} = \frac{1500 \text{ tokens}}{46.43 \text{ sec}} = 32.31 \text{ tokens/sec}$$

This metric tells us how many output tokens the entire system produced per second during the benchmark.

### Average Request Generation Rate: 16.16 tokens/sec

Each request's approximate rate is calculated as:

$$\text{Generation Rate} = \frac{\text{Output tokens}}{\text{Request latency}}$$

Your script calculates this for each request and takes the average.

### Key Differences

| Metric | Measurement |
|--------|-------------|
| **Aggregate throughput** | Total system output per second |
| **Average request generation rate** | Average per-request output rate |

> **Important:** Neither metric reflects the model's pure decode speed, because elapsed time includes request processing and potentially prompt processing overhead.
## 4. Understanding p50, p95, and p99

These are **latency percentiles** used in production monitoring to understand response time distributions.

### Example Interpretation

Imagine your application receives 1,000 requests:

| Percentile | Interpretation |
|-----------|-----------------|
| p50 = 2 sec | 50% of requests finish within 2 seconds |
| p95 = 5 sec | 95% of requests finish within 5 seconds |
| p99 = 10 sec | 99% of requests finish within 10 seconds |

### Your Results

Your p95 and p99 are both **9.59 seconds** because:
- Your benchmark contains only 10 requests
- Simple percentile calculation is used
- A sample this small is **not enough for reliable tail-latency analysis**

> **Recommendation:** Use larger sample sizes (e.g., 100+ requests) for more statistically meaningful percentile metrics.