# 🏥 Medical AI Expert — RAG-Based Medical Assistant

A full-stack AI-powered medical assistant built using **Flask**, **LangChain**, **Pinecone**, **Groq LLM**, and **HuggingFace embeddings**.

This system uses **Retrieval-Augmented Generation (RAG)** to provide context-aware medical responses based on a custom medical document knowledge base.

🌐 **Live Demo:** [https://medicalassistance-nmk.onrender.com](https://medicalassistance-nmk.onrender.com)

---

## 📌 Overview

Medical AI Expert is a web-based AI medical assistant that combines semantic search, document retrieval, vector databases, embeddings, and large language models.

The application retrieves relevant information from custom medical PDF documents and provides the retrieved context to the LLM before generating the final response.

The project also includes a **location-based hospital locator**, allowing users to find nearby hospitals using geolocation and map services.

> ⚠️ **Disclaimer:** This project is developed for educational and demonstration purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment.

---



## ✨ Key Features

- 🧠 Retrieval-Augmented Generation (RAG)
- 💬 Context-aware medical question answering
- 📚 Custom medical PDF knowledge base
- 🔎 Semantic similarity search using Pinecone
- 🧩 HuggingFace embeddings
- 🤖 Groq LLM integration
- 🔗 LangChain RAG pipeline
- 🌐 Interactive web-based chat interface
- 📍 Location-based hospital finder
- 🗺️ OpenStreetMap / Nominatim integration
- 🧭 Google Maps navigation support
- 🔐 Environment-variable based API configuration
- 🐳 Docker support
- ⚡ Gunicorn production server
- ☁️ Render deployment
- 📱 Responsive web interface

---



## 🏗️ System Architecture

```
┌───────────────────────┐
│      User Query       │
└──────────┬────────────┘
           ↓
┌───────────────────────┐
│      Flask App        │
└──────────┬────────────┘
           ↓
┌───────────────────────┐
│  HuggingFace          │
│  Embedding Model      │
└──────────┬────────────┘
           ↓
┌───────────────────────┐
│   Pinecone Vector DB  │
│   Similarity Search   │
└──────────┬────────────┘
           ↓
┌───────────────────────┐
│  Relevant Context     │
│     Top-K Chunks      │
└──────────┬────────────┘
           ↓
┌───────────────────────┐
│       Groq LLM        │
└──────────┬────────────┘
           ↓
┌───────────────────────┐
│     Final Answer      │
└───────────────────────┘
```

---



## 🔄 RAG Workflow

```
Medical PDF Documents
        ↓
Document Loading
        ↓
Text Extraction
        ↓
Text Chunking
        ↓
HuggingFace Embeddings
        ↓
Pinecone Vector Database
        ↓
User Query
        ↓
Query Embedding
        ↓
Semantic Similarity Search
        ↓
Relevant Context Retrieval
        ↓
Groq LLM
        ↓
Context-Aware Response
```



### 1️⃣ Document Loading

Medical PDF documents are placed inside the `data/` directory and loaded by the application.

### 2️⃣ Text Extraction

The application extracts text from the medical PDF documents.

### 3️⃣ Text Chunking

Large documents are divided into smaller chunks to improve retrieval performance and relevance.

### 4️⃣ Embedding Generation

HuggingFace embedding models convert the document chunks into numerical vector representations.

### 5️⃣ Vector Storage

The generated embeddings are stored in Pinecone for efficient similarity search.

### 6️⃣ Query Processing

When a user submits a question, the query is converted into an embedding.

### 7️⃣ Similarity Search

Pinecone searches the vector database and retrieves the most relevant document chunks.

### 8️⃣ Context Retrieval

The retrieved chunks are provided to the Groq LLM as contextual information.

### 9️⃣ Response Generation

The LLM generates a response using the user's question and retrieved medical context.

---



## ⚙️ Tech Stack


| Layer                   | Technology                |
| ----------------------- | ------------------------- |
| 🖥️ Backend             | Flask                     |
| 🐍 Programming Language | Python                    |
| 🧠 RAG Framework        | LangChain                 |
| 🤖 LLM                  | Groq                      |
| 🧠 Embeddings           | HuggingFace               |
| 📦 Vector Database      | Pinecone                  |
| 📄 PDF Processing       | PyPDF                     |
| 🎨 Frontend             | HTML, CSS, JavaScript     |
| 📍 Geolocation          | Browser Geolocation API   |
| 🗺️ Maps                | OpenStreetMap / Nominatim |
| 🧭 Navigation           | Google Maps               |
| 🚀 Deployment           | Render                    |
| ⚡ Production Server     | Gunicorn                  |
| 🐳 Containerization     | Docker                    |


---



## 📁 Project Structure

```
Medical_Assistant-RAG/
│
├── data/
│   └── Medical PDF Documents
│
├── src/
│   ├── helper.py
│   ├── prompt.py
│   └── __init__.py
│
├── templates/
│   └── chat.html
│
├── static/
│   └── style.css
│
├── app.py
├── store_index.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── .env
└── README.md
```

---



## 🚀 Installation



### 1️⃣ Clone the Repository

```
git clone <your-repository-url>
cd Medical_Assistant-RAG
```



### 2️⃣ Create Virtual Environment

```
python -m venv env
```



### 3️⃣ Activate Virtual Environment



#### Windows

```
env\Scripts\activate
```



#### Linux / macOS

```
source env/bin/activate
```



### 4️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---



## 🔐 Environment Variables

Create a `.env` file in the project root:

```
PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key
```

Never commit your `.env` file or expose API keys publicly.

Make sure `.env` is included in `.gitignore`.

---



## 📂 Data Preparation

Place your medical PDF documents inside the `data/` directory.

Example:

```
data/
├── medical_document_1.pdf
├── medical_document_2.pdf
└── medical_document_3.pdf
```

These documents are used as the knowledge base for the RAG pipeline.

---



## 🧠 Build the Pinecone Vector Index

Run:

```
python store_index.py
```

The indexing process performs the following steps:

```
Medical PDFs
     ↓
Load Documents
     ↓
Extract Text
     ↓
Split Text
     ↓
Generate Embeddings
     ↓
Upload Vectors
     ↓
Pinecone
```

---



## ▶️ Run the Application Locally

Start the Flask application:

```
python app.py
```

The application will be available at:

```
http://localhost:8080
```

Open the URL in your browser.

---



## 🌐 Live Deployment

The application is deployed on **Render**.

### Live Application

[https://medicalassistance-nmk.onrender.com](https://medicalassistance-nmk.onrender.com)

### Production Server

The deployed application uses Gunicorn:

```
gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120
```

Render provides the production port through the `$PORT` environment variable.

---



## 🐳 Docker Deployment



### Build Docker Image

```
docker build -t medical-ai .
```



### Run Container

```
docker run -p 8080:8080 \
  -e PINECONE_API_KEY=your_pinecone_api_key \
  -e GROQ_API_KEY=your_groq_api_key \
  medical-ai
```

Then open:

```
http://localhost:8080
```

---



## 💡 Example Queries

Users can ask questions such as:

- What is diabetes?
- What are the symptoms of diabetes?
- What are the symptoms of anxiety disorder?
- What are the causes of high blood pressure?
- What are the treatment options for acne?
- What are common symptoms of hypertension?
- What precautions should be taken for a particular condition?

The response is generated using the retrieved context from the configured medical knowledge base.

---



## 📍 Hospital Locator

The application also provides location-based hospital discovery.

### Workflow

```
User Location
      ↓
Browser Geolocation
      ↓
Latitude & Longitude
      ↓
Location Search
      ↓
Nearby Hospitals
      ↓
Google Maps Navigation
```

The hospital locator uses location services to help users discover nearby hospitals and navigate to them.

---



## 🔐 Security

API keys are stored using environment variables rather than hard-coded inside the source code.

Required environment variables:

```
PINECONE_API_KEY
GROQ_API_KEY
```

For local development, use `.env`.

For deployment, configure the variables through the hosting platform's environment-variable settings.

---



## ⚠️ Important Notes

- 📌 This project is intended for educational and demonstration purposes.
- ⚠️ It should not be used as a replacement for professional medical advice.
- 🩺 Users should consult qualified healthcare professionals for diagnosis and treatment.
- 📊 Response quality depends on the quality and coverage of the uploaded medical documents.
- 🔐 Never expose Pinecone or Groq API keys in source code.
- 📄 The RAG system can only provide information based on the configured knowledge base and LLM capabilities.

---



## 🚧 Future Improvements

- 🧠 Intelligent hospital recommendation system
- 🎤 Voice-based interaction
- 💾 Chat history and conversation memory
- 📈 Multi-document knowledge-base scaling
- 🗺️ Embedded interactive map using Leaflet
- 🎨 Advanced UI animations and themes
- 🔐 User authentication
- 📊 Analytics dashboard
- 🌍 Multi-language support
- 🧾 Medical report/document upload
- 🔎 Improved document citation and source display
- ⚡ Streaming LLM responses
- 🧠 Improved retrieval and reranking
- 📱 Progressive Web App support

---



## 📸 Application Preview

The application provides:

- Modern medical chatbot interface
- Medical question-answering functionality
- RAG-powered responses
- Hospital location functionality
- Responsive web interface

---



## 👨‍💻 Author

**Nagaram Manoj Kumar**

AI/ML Enthusiast | Full-Stack Developer

GitHub: **Zinb-NMK**

---



## 📜 License

This project is open-source and available under the **MIT License**.

---



## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---



## 🔗 Project Links

🌐 **Live Demo:** [https://medicalassistance-nmk.onrender.com](https://medicalassistance-nmk.onrender.com)

💻 **GitHub:** [https://github.com/Zinb-NMK](https://github.com/Zinb-NMK)

---



## 🏥 Medical AI Expert

Built with **Python • Flask • LangChain • Pinecone • Groq • HuggingFace • JavaScript**

**Retrieval-Augmented Generation for context-aware medical assistance.**