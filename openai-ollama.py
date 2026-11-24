from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key="ollama",
    base_url="http://localhost:11434/v1"
)

response = client.responses.create(
    model="llama3.2:1b",
    instructions="You are a funny guy with all assistant capability.",
    input="tell me about machine leanring under 20 words",
)

print(response.output_text)