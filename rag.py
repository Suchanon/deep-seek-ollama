import os
import sys

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import SKLearnVectorStore
import pickle
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# --- Configuration ---
PDF_PATH = "API testing _ Playwright.pdf"
DB_PATH = "./sklearn_db.json"
MODEL_NAME = "deepseek-coder-v2"
EMBEDDING_MODEL = "nomic-embed-text"

def ingest_pdf():
    """Reads PDF, splits text, and stores embeddings."""
    if not os.path.exists(PDF_PATH):
        print(f"Error: {PDF_PATH} not found.")
        sys.exit(1)

    print(f"Loading {PDF_PATH}...")
    loader = PyPDFLoader(PDF_PATH)
    pages = loader.load()
    
    print(f"Splitting {len(pages)} pages...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(pages)
    
    print(f"Embedding {len(chunks)} chunks into SKLearnVectorStore...")
    vectorstore = SKLearnVectorStore.from_documents(
        documents=chunks,
        embedding=OllamaEmbeddings(model=EMBEDDING_MODEL),
        persist_path=DB_PATH,
        serializer="json"
    )
    vectorstore.persist()
    print("Ingestion complete!")
    return vectorstore

def get_retriever():
    """Loads the existing vector store."""
    if not os.path.exists(DB_PATH):
        return ingest_pdf().as_retriever()
    
    vectorstore = SKLearnVectorStore(
        embedding=OllamaEmbeddings(model=EMBEDDING_MODEL),
        persist_path=DB_PATH,
        serializer="json"
    )
    return vectorstore.as_retriever()

def run_chat():
    """Interactive RAG chat loop."""
    print("Initializing RAG system...")
    retriever = get_retriever()
    llm = ChatOllama(model=MODEL_NAME)

    template = """Answer the question based ONLY on the following context:
    {context}
    
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    print("\n--- PDF Chat (Type 'quit' to exit) ---")
    while True:
        query = input("\nQuestion: ")
        if query.lower() in ["quit", "exit"]:
            break
        
        print("Thinking...", end=" ", flush=True)
        for chunk in chain.stream(query):
            print(chunk, end="", flush=True)
        print()

if __name__ == "__main__":
    run_chat()
