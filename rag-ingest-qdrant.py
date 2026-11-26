import json

from qdrant_client import QdrantClient, models
from fastembed import TextEmbedding

# Connect to Qdrant
client = QdrantClient(url="http://localhost:6333")

COLLECTION_NAME = "it_knowledge_walmart"

# Load documents
with open("documents/sample_docs.json", "r") as file:
    documents = json.load(file)

# Load open-source embedding model
embedding_model = TextEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Recreate collection
if client.collection_exists(COLLECTION_NAME):
    client.delete_collection(COLLECTION_NAME)

client.create_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=models.VectorParams(
        size=384,
        distance=models.Distance.COSINE
    )
)

# Generate embeddings and create Qdrant points
points = []

for doc in documents:

    embedding = list(
        embedding_model.embed([doc["content"]])
    )[0]

    points.append(
        models.PointStruct(
            id=doc["id"],
            vector=embedding.tolist(),
            payload={
                "title": doc["title"],
                "category": doc["category"],
                "content": doc["content"]
            }
        )
    )

# Insert into Qdrant
client.upsert(
    collection_name=COLLECTION_NAME,
    points=points
)

print("Documents ingested successfully!")
print("Collection:", COLLECTION_NAME)
print("Total documents:", len(points))

# Verify collection
info = client.get_collection(COLLECTION_NAME)
print("Stored points:", info.points_count)