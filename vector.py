from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

#Load dataset
df = pd.read_csv("data/goodreads_data.csv")

# Use embeddings for retrieval
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Set up ChromaDB storage
db_location = "./chroma_book_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    for i, row in df.iterrows():
        document = Document(
            page_content = row["Description"],
            metadata={
                "title": row["Book"],
                "author": row["Author"],
                "genres": row["Genres"],
                "rating": row["Avg_Rating"]
            },
            id = str(i)
        )
        ids.append(str(i))
        documents.append(document)

# Initialize vector store
vector_store = Chroma(
    collection_name = "book_recommendations",
    persist_directory = db_location,
    embedding_function = embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

# Create retriever to fetch top 5 books
retriever = vector_store.as_retriever(search_kwargs={"k": 5})