from typing import List
import logging

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_core.documents import Document


# =========================
# CONFIG
# =========================

PERSIST_DIRECTORY = "chroma"
EMBEDDING_MODEL = "nomic-embed-text"
LLM_MODEL = "mistral"
TOP_K = 8


# =========================
# LOGGING
# =========================

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# =========================
# PROMPT
# =========================

RAG_PROMPT = """
You are a precise question-answering system.

Answer ONLY using the provided context.
If the answer is not explicitly contained in the context, respond with:

"I cannot answer based on the provided context."

Rules:
- be concise
- no explanations
- no assumptions
- no external knowledge

Context:
{context}

Question:
{question}

Answer:
"""


# =========================
# CORE FUNCTIONS
# =========================

def _load_embeddings() -> OllamaEmbeddings:
    return OllamaEmbeddings(model=EMBEDDING_MODEL)


def _load_vectorstore(embeddings: OllamaEmbeddings) -> Chroma:
    return Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embeddings
    )


def _retrieve_docs(db: Chroma, question: str) -> List[Document]:
    return db.similarity_search(question, k=TOP_K)


def _format_context(docs: List[Document]) -> str:
    return "\n\n".join(doc.page_content for doc in docs)


def _build_prompt(context: str, question: str) -> str:
    return RAG_PROMPT.format(context=context, question=question)


def _load_llm() -> Ollama:
    return Ollama(model=LLM_MODEL)


# =========================
# PUBLIC API
# =========================

def ask_rag(question: str) -> str:
    logger.info("Loading embeddings...")
    embeddings = _load_embeddings()

    logger.info("Loading vector store...")
    db = _load_vectorstore(embeddings)

    logger.info("Retrieving relevant documents...")
    docs = _retrieve_docs(db, question)

    if not docs:
        return "No relevant context found."

    context = _format_context(docs)
    prompt = _build_prompt(context, question)

    llm = _load_llm()

    logger.info("Generating answer...")

    try:
        return llm.invoke(prompt)
    except Exception as e:
        logger.warning(f"invoke() failed: {e}")

        try:
            return llm(prompt)
        except Exception as e2:
            logger.warning(f"direct call failed: {e2}")

            if hasattr(llm, "generate"):
                gen = llm.generate([prompt])
                return gen.generations[0][0].text

            raise RuntimeError("LLM execution failed completely")
