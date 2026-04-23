from dotenv import load_dotenv
import os
from src.helper import (
    load_pdf_file,
    filter_to_minimal_docs,
    text_split,
    download_hugging_face_embeddings
)
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

# ---------- load environment ----------
load_dotenv()

# ---------- env variables ----------
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

if not PINECONE_API_KEY:
    raise ValueError("❌ PINECONE_API_KEY is missing in .env file")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# ---------- data ingestion ----------
print("📄 Loading PDFs...")
extracted_data = load_pdf_file(data="data/")

print("🧹 Filtering data...")
filter_data = filter_to_minimal_docs(extracted_data)

print("✂️ Splitting text into chunks...")
text_chunks = text_split(filter_data)

print("🧠 Loading embeddings model...")
embeddings = download_hugging_face_embeddings()

# ---------- Pinecone setup ----------
print("🔗 Connecting to Pinecone...")
pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medicalassistant"   # ✅ MUST match your Pinecone index

# ---------- create index if not exists ----------
if not pc.has_index(index_name):
    print("⚠️ Index not found. Creating new index...")
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        ),
    )
else:
    print("✅ Index already exists")

# ---------- store vectors ----------
print("📤 Uploading embeddings to Pinecone...")
PineconeVectorStore.from_documents(
    documents=text_chunks,
    embedding=embeddings,
    index_name=index_name,
)

print("🎉 Indexing completed successfully!")