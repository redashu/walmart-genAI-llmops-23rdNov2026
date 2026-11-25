FROM  ghcr.io/ggml-org/llama.cpp:server

COPY  models-llm/SmolLM2-360M-Instruct-Q4_K_M.gguf /models/model.gguf 

EXPOSE 8080

CMD ["-m","/models/model.gguf","--host","0.0.0.0","--port","8080","-c","2048","-t","4"] 