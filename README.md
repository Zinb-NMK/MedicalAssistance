# 🏥 Medical AI Expert — RAG-Based Chatbot

A full-stack AI-powered medical assistant built using **Flask**, **Pinecone**, **Groq LLM**, and **HuggingFace embeddings**.
This system uses **Retrieval-Augmented Generation (RAG)** to provide accurate, context-aware medical answers from custom PDF data.

---

## 📌 Overview

This project implements a real-world AI architecture where user queries are answered by combining:

* 🔍 Semantic search (vector database)
* 📄 Context retrieval from medical documents
* 🤖 Large Language Model (LLM) reasoning

The system ensures responses are grounded in actual data rather than purely generated text.

---

## ✨ Key Features

* 🧠 Retrieval-Augmented Generation (RAG) pipeline
* 💬 Context-aware medical question answering
* ⚡ Fast inference using Groq (LLaMA 3)
* 🔎 Vector similarity search with Pinecone
* 📚 Custom knowledge base using PDF documents
* 🌐 Interactive web-based chat interface
* 🧩 Modular and scalable backend design

---

## 🏗️ System Architecture

```
┌───────────────────────┐
│      User Query       │
└──────────┬────────────┘
           ↓
┌───────────────────────┐
│  Embedding Model      │
│  (HuggingFace)        │
└──────────┬────────────┘
           ↓
┌───────────────────────┐
│   Pinecone Vector DB  │
│ (Similarity Search)   │
└──────────┬────────────┘
           ↓
┌───────────────────────┐
│  Top-K Context Chunks │
└──────────┬────────────┘
           ↓
┌───────────────────────┐
│   Groq LLM (LLaMA 3)  │
└──────────┬────────────┘
           ↓
┌───────────────────────┐
│     Final Answer      │
└───────────────────────┘
```

---

## ⚙️ Tech Stack

| Layer        | Technology            |
| ------------ | --------------------- |
| 🖥 Backend   | Flask (Python)        |
| 🤖 LLM       | Groq (LLaMA 3)        |
| 🧠 Embedding | HuggingFace           |
| 📦 Vector DB | Pinecone              |
| 🎨 Frontend  | HTML, CSS, JavaScript |

---

## 📁 Project Structure

```
RAG-LLM-medical-chatbot/
│
├── data/                  # Medical PDFs (knowledge base)
├── src/
│   ├── helper.py          # Data loading & preprocessing
│   ├── prompt.py          # Prompt engineering
│   └── __init__.py
│
├── templates/
│   └── chat.html          # Chat UI
│
├── static/
│   └── style.css          # UI styling
│
├── app.py                 # Flask application
├── store_index.py         # Embedding + Pinecone upload
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

---

## 🚀 Installation

### 1️⃣ Clone Repository

```
git clone <your-repo-url>
cd RAG-LLM-medical-chatbot
```

### 2️⃣ Create Virtual Environment

```
python -m venv env
env\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in root directory:

```
PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key
```

---

## 📂 Data Preparation

Place your medical PDF files inside:

```
data/
```

---

## 🧠 Build Vector Index

```
python store_index.py
```

✔ Loads PDFs
✔ Splits text into chunks
✔ Generates embeddings
✔ Uploads to Pinecone

---

## ▶️ Run Application

```
python app.py
```

Open in browser:

```
http://localhost:8080
```

---

## 💡 Example Queries

* What is diabetes?
* Symptoms of anxiety disorder
* Treatment options for acne
* Causes of high blood pressure

---

## 🐳 Docker Deployment (Optional)

```
docker build -t medical-ai .
docker run -p 8080:8080 -e PINECONE_API_KEY=your_key -e GROQ_API_KEY=your_key medical-ai
```

---

## ⚠️ Important Notes

* 📌 For educational purposes only
* ⚠️ Not a substitute for professional medical advice
* 📊 Accuracy depends on uploaded data

---

## 🚧 Future Improvements

* 📍 Hospital locator integration
* 🎤 Voice-based interaction
* 💾 Chat memory & history
* 📈 Multi-document scaling
* 🎨 Advanced UI (animations & themes)

---

## 👨‍💻 Author

**Nagaram Manoj Kumar**
AI/ML Enthusiast | Full-Stack Developer

---

## 📜 License

This project is open-source under the MIT License.
