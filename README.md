# SahakarBot - Backend

![SahakarBot Banner](https://img.shields.io/badge/SahakarBot-Legal%20Assistant-blue?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B6B?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)

**An intelligent AI chatbot for the Maharashtra Co-operative Societies Act, 1960**

[Frontend Repo](https://github.com/omrawal/SahakarBot-Frontend) | [Watch Tutorial](https://youtu.be/NdayU-saFXg) | [Live Demo](#)

---

## 📺 Video Tutorial

**[▶️ Watch: I Built an AI Legal Assistant in 15 Minutes](https://youtu.be/NdayU-saFXg)**

Complete walkthrough covering:
- FastAPI backend setup
- LangChain RAG implementation
- ChromaDB vector database
- Perplexity AI integration
- Deployment to Google Cloud Run

---

## 🎯 About

SahakarBot is an intelligent chatbot designed to help users navigate and understand **The Maharashtra Co-operative Societies Act, 1960**. By uploading the official PDF or querying directly, SahakarBot provides quick, accurate, and contextual answers to your legal questions using advanced RAG (Retrieval Augmented Generation) technology.

### ✨ Key Features

- 📄 **PDF Processing**: Automatically extracts and chunks legal documents
- 🧠 **Semantic Search**: Vector database powered similarity search
- 💬 **Context-Aware Chat**: Maintains conversation history for follow-up questions
- ⚡ **Fast Response**: Optimized retrieval with ChromaDB indexing
- 🔒 **Accurate Answers**: Uses Perplexity AI for factual, grounded responses
- 🚀 **Production Ready**: Dockerized and deployable to Cloud Run

---

## 🏗️ Architecture

```
User Query
    ↓
FastAPI Backend (CORS Middleware, /query endpoint)
    ↓
LangChain RAG Pipeline
    ├─ Query Embedding
    ├─ Vector Search
    ├─ Context Retrieval
    └─ LLM Generation
    ↓
    ├─ ChromaDB (Vector Store with HuggingFace Embeddings)
    └─ Perplexity AI (LLM Response)
    ↓
Response to Frontend
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **FastAPI** | Backend API framework |
| **LangChain** | RAG orchestration |
| **ChromaDB** | Vector database for embeddings |
| **HuggingFace** | Sentence embeddings (all-MiniLM-L6-v2) |
| **Perplexity AI** | LLM for answer generation |
| **PyPDFLoader** | PDF document processing |
| **Docker** | Containerization |
| **Google Cloud Run** | Serverless deployment |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Perplexity AI API Key

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/omrawal/SahakarBot-Backend.git
cd SahakarBot-Backend
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate
```

On Windows: `venv\Scripts\activate`

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set environment variables**

```bash
export PERPLEXITY_API_KEY="your-api-key-here"
```

5. **Run the server**

```bash
uvicorn main:app --reload --port 8000
```

API will be available at `http://localhost:8000`

---

## 📚 API Documentation

### POST /query

Send a question with optional chat history.

**Request Body:**

```json
{
  "question": "What is the registration process?",
  "chat_history": [
    {
      "question": "What is section 25?",
      "answer": "Section 25 deals with membership eligibility..."
    }
  ]
}
```

**Response:**

```json
{
  "answer": "To register a cooperative society under the Maharashtra Act..."
}
```

---

## 🐳 Docker Deployment

### Build Image

```bash
docker build -t sahakarbot-backend .
```

### Run Container

```bash
docker run -p 8080:8080 \
  -e PERPLEXITY_API_KEY="your-key" \
  sahakarbot-backend
```

### Deploy to Google Cloud Run

```bash
gcloud builds submit --tag gcr.io/PROJECT_ID/sahakarbot-backend

gcloud run deploy sahakarbot-backend \
  --image gcr.io/PROJECT_ID/sahakarbot-backend \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

---

## 📁 Project Structure

```
SahakarBot-Backend/
├── main.py              # FastAPI application
├── query.py             # RAG pipeline implementation
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker configuration
├── chroma_db/          # Vector database storage
└── README.md           # This file
```

---

## 🔧 Configuration

### Key Parameters

**Text Chunking:**
- Chunk Size: 1000 characters
- Chunk Overlap: 200 characters

**Vector Search:**
- Embedding Model: all-MiniLM-L6-v2
- Retrieval: Top 3 most relevant chunks

**LLM:**
- Model: Perplexity AI (llama-3.1-sonar)
- Temperature: 0.2 (for factual responses)

---

## 🌐 Related Repositories

- **Frontend**: [SahakarBot-Frontend](https://github.com/omrawal/SahakarBot-Frontend) - React chatbot interface

---

## 🎥 Tutorial Video

Learn how to build this project step-by-step:

**[I Built an AI Legal Assistant in 15 Minutes (FastAPI + LangChain + ChromaDB Tutorial)](https://youtu.be/NdayU-saFXg)**

Topics covered:
- PDF processing & text chunking
- Vector databases & embeddings
- LangChain RAG pipeline
- FastAPI integration
- Docker & Cloud Run deployment

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Om Rawal**

- GitHub: [@omrawal](https://github.com/omrawal)
- YouTube: [Watch Tutorial](https://youtu.be/NdayU-saFXg)

---

## 🙏 Acknowledgments

- [LangChain](https://python.langchain.com/) - RAG framework
- [ChromaDB](https://www.trychroma.com/) - Vector database
- [FastAPI](https://fastapi.tiangolo.com/) - Web framework
- [Perplexity AI](https://www.perplexity.ai/) - LLM provider

---

**⭐ Star this repo if you found it helpful!**

[Backend](https://github.com/omrawal/SahakarBot-Backend) | [Frontend](https://github.com/omrawal/SahakarBot-Frontend) | [Tutorial](https://youtu.be/NdayU-saFXg)
