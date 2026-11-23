from transformers import AutoTokenizer

model_path = "models/SmolLM2-360M-Instruct"
# location where you downloaded or saved the model locally

tokenizer = AutoTokenizer.from_pretrained(model_path)

text = "How do I troubleshoot a Docker container?"

tokens = tokenizer.tokenize(text)
token_ids = tokenizer.encode(text)

print("Original text:", text)
print("Tokens:", tokens)
print("Token IDs:", token_ids)
print("Token count:", len(token_ids))