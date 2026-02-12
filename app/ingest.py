import logging
from pathlib import Path
from typing import List

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


# =========================
# CONFIG
# =========================

DATA_DIR = "data"
PERSIST_DIRECTORY = "chroma"
EMBEDDING_MODEL = "nomic-embed-text"

CHUNK_SIZE = 800
CHUNK_OVERLAP = 100


# =========================
# LOGGING
# =========================

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# =========================
# LOAD FILES
# =========================

def load_txt_files(directory: str) -> List[Document]:
    docs = []
    for path in Path(directory).glob("*.txt"):
        text = path.read_text(encoding="utf-8")
        docs.append(Document(page_content=text, metadata={"source": str(path)}))
    return docs


# =========================
# SPLIT
# =========================

def split_documents(docs: List[Document]) -> List[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.split_documents(docs)


# =========================
# INGEST
# =========================

def run_ingestion():
    logger.info("Loading documents...")
    raw_docs = load_txt_files(DATA_DIR)

    if not raw_docs:
        raise ValueError("No documents found in data directory.")

    logger.info(f"{len(raw_docs)} documents loaded")

    logger.info("Splitting documents...")
    chunks = split_documents(raw_docs)
    logger.info(f"{len(chunks)} chunks created")

    logger.info("Loading embeddings...")
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)

    logger.info("Creating vector store...")
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=PERSIST_DIRECTORY
    )

    db.persist()
    logger.info("Ingestion complete.")

