from qdrant_client import QdrantClient
from fastembed import TextEmbedding

client = QdrantClient(url="http://localhost:6333")

embedding_model = TextEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

COLLECTION_NAME = "it_knowledge"

query = "How can I automatically increase application instances?"

# Convert query into embedding
query_vector = list(
    embedding_model.query_embed(query)
)[0]

# Search Qdrant
results = client.query_points(
    collection_name=COLLECTION_NAME,
    query=query_vector.tolist(),
    limit=3
).points

print("\nSearch Query:", query)
print("\nTop Matching Documents:\n")

for result in results:
    print("Title:", result.payload["title"])
    print("Category:", result.payload["category"])
    print("Score:", round(result.score, 4))
    print("Content:", result.payload["content"])
    print("-" * 60)
