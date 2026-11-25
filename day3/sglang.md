# SGLang: LLM Inference and Serving Framework

**SGLang** is an open-source LLM inference and serving framework developed by **LMSYS**, the organization associated with **Chatbot Arena**. It is not a Hugging Face product, although it integrates closely with the Hugging Face model ecosystem.

> Its main purpose is to serve LLMs efficiently, particularly when handling many concurrent requests, long prompts, and agentic workloads.

📚 [SGLang Documentation](https://github.com/lmsys/sglang)

---

## 1. What Makes SGLang Interesting?

### The Standout Feature: RadixAttention

Imagine **100 users** interacting with the same AI assistant. Every request contains the same system prompt:

```
You are an IT support assistant.
You help users troubleshoot Linux, Docker and Kubernetes.
```

**Without prefix caching**, the inference engine may repeatedly compute attention states for this shared prefix.

**SGLang uses RadixAttention** to manage and reuse KV-cache entries for shared prefixes.

#### Without Prefix Caching ❌

```
Request 1: Shared prompt → Compute
Request 2: Shared prompt → Compute
Request 3: Shared prompt → Compute
```

#### With SGLang Prefix Caching ✅

```
Shared prompt → Compute once and cache
├── Request 1 → Reuse cache
├── Request 2 → Reuse cache
└── Request 3 → Reuse cache
```

> This can reduce repeated computation and improve **throughput and latency** when requests share prefixes.

📚 [SGLang Documentation - RadixAttention](https://github.com/lmsys/sglang)

---

## 2. Major SGLang Features

| Feature | What It Does |
|---------|-------------|
| **RadixAttention** | Reuses KV-cache entries for common prefixes |
| **Continuous batching** | Dynamically schedules incoming requests |
| **Paged attention** | Efficient KV-cache memory management |
| **Tensor parallelism** | Distributes model computation across GPUs |
| **Pipeline parallelism** | Distributes model layers across devices |
| **Speculative decoding** | Uses draft tokens to accelerate generation |
| **Structured outputs** | Supports constrained JSON and structured generation |
| **Multi-LoRA** | Serves multiple LoRA adapters efficiently |
| **Multimodal serving** | Supports vision, audio, and other model workloads |

> These are among the capabilities described in the official project documentation.

📚 [SGLang GitHub Repository](https://github.com/lmsys/sglang)

---

## 3. TGI vs vLLM vs SGLang

| Capability | TGI | vLLM | SGLang |
|------------|-----|------|--------|
| **Organization** | Hugging Face | vLLM project | LMSYS |
| **Model ecosystem** | Hugging Face | Hugging Face and others | Hugging Face and others |
| **Continuous batching** | ✅ Yes | ✅ Yes | ✅ Yes |
| **KV-cache optimization** | Yes | PagedAttention | RadixAttention |
| **OpenAI-compatible API** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Multi-GPU serving** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Agentic workloads** | General serving | General serving | 💪 Strong focus |

> **Important Distinction**: TGI is in **maintenance mode**, whereas **vLLM** and **SGLang** are actively developed inference frameworks.

---

## 4. SGLang Architecture

Think of SGLang as several components working together:

```
┌──────────────────────────────────────────────────────┐
│          API Layer                                   │
│    (Accepts client requests)                         │
└───────────────────┬──────────────────────────────────┘
                    │
┌───────────────────▼──────────────────────────────────┐
│          Scheduler                                   │
│    (Manages incoming requests)                       │
└───────────────────┬──────────────────────────────────┘
                    │
┌───────────────────▼──────────────────────────────────┐
│          RadixAttention                              │
│    (Manages reusable KV-cache blocks)                │
└───────────────────┬──────────────────────────────────┘
                    │
┌───────────────────▼──────────────────────────────────┐
│          Model Execution Engine                      │
│    (Executes Transformer layers)                     │
└───────────────────┬──────────────────────────────────┘
                    │
┌───────────────────▼──────────────────────────────────┐
│          GPU/CPU Memory                              │
│    (Weights, activations, KV cache)                  │
└──────────────────────────────────────────────────────┘
```

---

## 5. How Do We Deploy SGLang?

SGLang supports **Docker** and **Python-based installation**. Its official documentation provides both approaches.

📚 [SGLang GitHub - Installation](https://github.com/lmsys/sglang)

### For NVIDIA GPU Ubuntu Machine: Docker Approach

**Step 1: Pull the Docker image**

```bash
docker pull lmsysorg/sglang:latest
```

**Step 2: Run the SGLang container**

```bash
docker run -d \
  --name sglang-server \
  --gpus all \
  --shm-size 32g \
  -p 30000:30000 \
  -v ~/LLMOps-Lab/models:/models \
  lmsysorg/sglang:latest \
  python3 -m sglang.launch_server \
    --model-path /models/SmolLM2-360M-Instruct \
    --host 0.0.0.0 \
    --port 30000
```

**Step 3: Test the API**

```bash
curl http://localhost:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "SmolLM2-360M-Instruct",
    "messages": [
      {"role": "user", "content": "Explain Docker"}
    ],
    "max_tokens": 100
  }'
```

### Docker Run Parameters

| Parameter | Purpose |
|-----------|---------|
| `-d` | Run container in background |
| `--name sglang-server` | Container name |
| `--gpus all` | Enable GPU access |
| `--shm-size 32g` | Shared memory for GPU communication |
| `-p 30000:30000` | Port mapping (host:container) |
| `-v ~/LLMOps-Lab/models:/models` | Mount local model directory |
| `--model-path` | Path to model inside container |
| `--host 0.0.0.0` | Listen on all interfaces |
| `--port 30000` | Server port |

---

## 6. Important Hardware Note ⚠️

> **This is a GPU deployment example**, not a command to run on your current CPU-only lab. The current official installation guidance primarily targets **Linux with supported accelerators**, and **hardware-specific compatibility must be checked**.

---

## Summary

| Aspect | Details |
|--------|---------|
| **What is SGLang?** | Open-source LLM inference framework by LMSYS |
| **Key Feature** | RadixAttention for prefix caching |
| **Main Use Case** | Efficient serving with concurrent requests |
| **Deployment** | Docker or Python-based installation |
| **API** | OpenAI-compatible chat completions |
| **Status** | 🟢 Actively developed |
| **Best For** | Agentic workloads, production serving |