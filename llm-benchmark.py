from openai import OpenAI
from concurrent.futures import ThreadPoolExecutor
from time import perf_counter
from statistics import mean

client = OpenAI(
    base_url="http://localhost:8082/v1",
    api_key="no-key-required",
    max_retries=0,
    timeout=120
)

MODEL = "SmolLM2-360M-Instruct"

def send_request(number):
    prompt = (
        f"Request {number}: Explain Docker containers "
        "and Kubernetes in simple terms."
    )

    start = perf_counter()

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )

        elapsed = perf_counter() - start
        tokens = response.usage.completion_tokens

        return {
            "success": True,
            "latency": elapsed,
            "tokens": tokens,
            "tokens_per_sec": tokens / elapsed
        }

    except Exception as e:
        return {
            "success": False,
            "latency": perf_counter() - start,
            "error": str(e)
        }

# Change this to demonstrate different workloads
TOTAL_REQUESTS = 10
CONCURRENCY = 2

start = perf_counter()

with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
    results = list(executor.map(send_request, range(TOTAL_REQUESTS)))

total_time = perf_counter() - start

successful = [r for r in results if r["success"]]
failed = [r for r in results if not r["success"]]

latencies = sorted(r["latency"] for r in successful)

def percentile(values, p):
    if not values:
        return 0
    index = round((len(values) - 1) * p / 100)
    return values[index]

print("\n===== LLM BENCHMARK =====")
print("Total requests:", TOTAL_REQUESTS)
print("Successful:", len(successful))
print("Failed:", len(failed))
print("Total duration:", round(total_time, 2), "seconds")

if successful:
    print("Average latency:", round(mean(latencies), 2), "sec")
    print("p50 latency:", round(percentile(latencies, 50), 2), "sec")
    print("p95 latency:", round(percentile(latencies, 95), 2), "sec")
    print("p99 latency:", round(percentile(latencies, 99), 2), "sec")

    total_tokens = sum(r["tokens"] for r in successful)
    print("Total output tokens:", total_tokens)
    print("Aggregate throughput:", round(total_tokens / total_time, 2),
          "tokens/sec")
    print("Average request generation rate:",
          round(mean(r["tokens_per_sec"] for r in successful), 2),
          "tokens/sec")

if failed:
    print("\nErrors:")
    for r in failed:
        print(r["error"])