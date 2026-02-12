# 🧠 Local RAG System — Production‑Style AI Retrieval Pipeline

A fully local **Retrieval Augmented Generation (RAG)** system built with modern AI infrastructure patterns.

This project demonstrates how to build a **privacy‑first, production‑ready question answering system** that retrieves knowledge from custom documents and generates grounded answers using local LLMs.

No external APIs. No cloud dependency. Fully offline.

---

# ✨ Why this project exists

Most AI demos rely on cloud APIs and toy datasets.

This project focuses on what **real AI systems look like in production**:

✔ Document ingestion pipeline
✔ Semantic chunking
✔ Embedding generation
✔ Vector database retrieval
✔ Context‑grounded LLM responses
✔ API layer for consumption
✔ Strict hallucination control
✔ Fully local infrastructure

This is not a chatbot.
This is an **AI knowledge system**.

---

# 🏗 System Architecture

```
Documents (PDF / TXT / MD)
        ↓
Text Chunking
        ↓
Embeddings (nomic-embed-text)
        ↓
Vector Database (ChromaDB)
        ↓
Similarity Retrieval
        ↓
Context Injection
        ↓
Local LLM (Mistral via Ollama)
        ↓
Grounded Answer
        ↓
FastAPI Endpoint
```

---

# 🧩 Tech Stack

### AI / ML

* Local LLM → Mistral (Ollama)
* Embeddings → nomic-embed-text
* Framework → LangChain

### Retrieval

* Vector DB → Chroma
* Semantic search → cosine similarity

### Backend

* FastAPI
* Pydantic
* Uvicorn

### Infrastructure

* Python virtual environments
* Fully local inference
* No external API calls

---

# 🔒 Privacy First Design

All processing happens locally:

✔ Documents never leave your machine
✔ Embeddings generated locally
✔ LLM inference local
✔ Vector DB local
✔ No telemetry
✔ No API keys

This architecture is ideal for:

* Enterprise internal knowledge bases
* Legal document search
* Financial reports
* Medical literature (offline environments)
* Secure environments

---

# 📁 Project Structure

```
demo-rag-local/
│
├── app/
│   ├── main.py        # FastAPI application
│   ├── ingest.py      # Document ingestion pipeline
│   └── rag.py         # Retrieval + generation logic
│
├── data/
│   └── docs/          # Source documents
│
├── chroma/            # Vector database (auto-generated)
│
├── requirements.txt
└── README.md
```

---

# 🚀 Quick Start

## 1. Install Ollama

Mac:

```bash
brew install ollama
ollama serve
```

---

## 2. Download local models

```bash
ollama pull mistral
ollama pull nomic-embed-text
```

---

## 3. Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Add documents

Place files inside:

```
data/docs/
```

Supported formats:

* PDF
* TXT
* Markdown

---

## 6. Run ingestion pipeline

```bash
python app/ingest.py
```

This will:

✔ Load documents
✔ Split into semantic chunks
✔ Generate embeddings
✔ Store vectors in Chroma

---

## 7. Start API server

```bash
python -m uvicorn app.main:app --reload
```

Server:

```
http://127.0.0.1:8000
```

---

# 💬 Query the system

## Swagger UI

```
http://127.0.0.1:8000/docs
```

POST `/question`

```json
{
  "question": "Your question here"
}
```

---

## Terminal request

```bash
curl -X POST "http://127.0.0.1:8000/question" \
-H "Content-Type: application/json" \
-d '{"question": "What is RAG?"}'
```

---

# 🧠 How hallucination is prevented

The LLM is strictly instructed to answer **only using retrieved context**.

If no relevant context exists → the model must respond:

```
I cannot answer based on the provided context.
```

This ensures:

✔ Grounded responses
✔ Deterministic behavior
✔ Enterprise reliability

---

# ⚙ Core Components

## Ingestion Pipeline

* Document loading
* Recursive text splitting
* Embedding generation
* Vector persistence

## Retrieval Layer

* Top‑K similarity search
* Context assembly
* Relevance filtering

## Generation Layer

* Context injection prompt
* Local LLM inference
* Controlled response policy

## API Layer

* Request validation
* RAG orchestration
* JSON response

---

# 📊 Performance Characteristics

Depends on hardware.

Typical laptop performance:

* Embedding generation → fast (CPU ok)
* Retrieval → < 100ms
* LLM response → 1–4 seconds

---

# 🎯 Real World Use Cases

* Internal company knowledge search
* Customer support automation
* Compliance document lookup
* Technical documentation assistant
* Research paper QA
* Offline AI environments

---

# 🧪 Example Questions

✔ "Summarize the policy document"
✔ "What are the safety requirements?"
✔ "Explain section 3.2"
✔ "What deadlines are mentioned?"

---

# 🔮 Future Improvements

* Streaming responses
* Hybrid search (BM25 + vector)
* Re-ranking models
* Evaluation metrics (RAGAS)
* Web UI
* Docker container
* Multi‑document collections
* Authentication layer
* Observability / tracing

---

# 🧑‍💻 Author

**Alex Victor de Andrade**
AI Engineer | Full‑Stack Developer | Applied AI Systems

Focus areas:

* Retrieval systems
* Generative AI infrastructure
* LLM applications
* Production AI architecture

---

# ⭐ If this project helped you

Consider giving it a star and sharing feedback.

---

# 📜 License

MIT License
