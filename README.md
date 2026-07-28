# 🚀 AskDSA - AI-Powered DSA RAG Engine

AskDSA is an intelligent **Retrieval-Augmented Generation (RAG)** platform that answers **Data Structures & Algorithms (DSA)** questions using a hybrid retrieval pipeline. It combines lexical search, semantic search, reranking, and Large Language Models (LLMs) to generate accurate, context-aware responses with reduced hallucinations.

---

## ✨ Features

* 📚 Ask natural language DSA questions
* 🔍 Hybrid Retrieval (BM25 + Vector Search)
* ⚡ Reciprocal Rank Fusion (RRF)
* 🎯 Maximum Marginal Relevance (MMR) for diverse context retrieval
* 🧠 Cross-Encoder Reranking
* 🤖 Google Gemini LLM Integration
* 📄 PDF ingestion and preprocessing
* ✂️ Intelligent document chunking
* 🧩 HuggingFace Sentence Transformer embeddings
* 🗂️ ChromaDB vector database
* 🌐 FastAPI backend
* 💻 Node.js + Express.js API gateway
* 🎨 Interactive frontend interface
* 📈 Designed for scalable knowledge bases (20K+ embeddings)

---

# 🏗️ Architecture

```
User Query
     │
     ▼
Node.js / Express API
     │
     ▼
FastAPI Backend
     │
     ▼
Hybrid Retrieval Pipeline
     ├── BM25 Search
     ├── Vector Search
     ├── RRF Fusion
     ├── MMR
     └── Cross Encoder Reranker
     │
     ▼
Gemini LLM
     │
     ▼
Generated Answer
```

---

# 📁 Project Structure

```
AskDSA/
│
├── Backend/
│   ├── server.js
│   ├── package.json
│   └── ...
│
├── Frontend/
│   ├── index.html
│   ├── styles.css
│   ├── script.js
│   └── ...
│
├── Rag/
│   ├── ingestion/
│   ├── retrieval/
│   ├── llm/
│   ├── data/
│   ├── api.py
│   ├── app.py
│   └── ...
│
└── README.md
```

---

# ⚙️ Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Node.js
* Express.js
* FastAPI
* Python

### AI & RAG

* Google Gemini API
* HuggingFace Sentence Transformers
* ChromaDB
* BM25
* Reciprocal Rank Fusion (RRF)
* Maximum Marginal Relevance (MMR)
* Cross Encoder Reranker

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/VedantRalekar/AskDSA.git
cd AskDSA
```

---

## 2. Backend

```bash
cd Backend
npm install
npm start
```

---

## 3. Python Environment

```bash
cd Rag

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file inside the `Rag` directory.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## 5. Start FastAPI

```bash
python -m uvicorn api:app --reload
```

---

## 6. Open Frontend

Open the frontend in your browser.

```
http://localhost:3000
```

or

```
index.html
```

depending on your setup.

---

# 🔄 Retrieval Pipeline

```
PDF Documents
      │
      ▼
Cleaning
      │
      ▼
Chunking
      │
      ▼
Embedding Generation
      │
      ▼
ChromaDB Storage
      │
      ▼
User Query
      │
      ▼
BM25 Search
      │
      ▼
Vector Search
      │
      ▼
RRF Fusion
      │
      ▼
Cross Encoder Reranking
      │
      ▼
Gemini LLM
      │
      ▼
Final Response
```

---

# 📊 Key Capabilities

* Hybrid search improves retrieval quality
* Semantic understanding using transformer embeddings
* Reduced hallucinations through context-aware generation
* Modular RAG architecture
* Efficient retrieval over 20K+ embeddings
* Metadata-aware document retrieval
* Easily extensible for additional datasets

---

# 📸 Demo

Add screenshots or a GIF here.

```
<img src="[https://raw.githubusercontent.com/VedantRalekar/AskDSA/main/assets/home.png](https://github.com/VedantRalekar/AskDSA/blob/5da0f49111f04eaac4ea9f771fb3d9a725fc2735/Screenshot%202026-07-28%20184819.png)" width="100%">
```

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

# 👨‍💻 Author

**Vedant Ralekar**

* GitHub: https://github.com/VedantRalekar

---

⭐ If you found this project useful, consider giving it a star on GitHub!
