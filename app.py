from flask import Flask, render_template, jsonify, request
import requests
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore

from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

app = Flask(__name__)
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

rag_chain = None


def get_rag_chain():
    global rag_chain
    if rag_chain is not None:
        return rag_chain

    embeddings = download_hugging_face_embeddings()
    docsearch = PineconeVectorStore.from_existing_index(
        index_name="medicalassistant",
        embedding=embeddings,
    )
    retriever = docsearch.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3},
    )
    chat_model = ChatGroq(
        model="openai/gpt-oss-20b",
        groq_api_key=GROQ_API_KEY,
        temperature=0,
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )
    question_answer_chain = create_stuff_documents_chain(chat_model, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    return rag_chain


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    response = get_rag_chain().invoke({"input": msg})
    return str(response["answer"])


@app.route("/hospitals", methods=["POST"])
def get_hospitals():
    lat = float(request.form.get("lat"))
    lon = float(request.form.get("lon"))

    delta = 0.05
    viewbox = f"{lon - delta},{lat - delta},{lon + delta},{lat + delta}"

    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": "hospital",
        "format": "json",
        "limit": 5,
        "bounded": 1,
        "viewbox": viewbox,
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers={"User-Agent": "medical-chatbot"},
            timeout=10,
        )
        data = response.json()
    except Exception:
        return jsonify({"error": True})

    hospitals = []
    for place in data:
        hospitals.append({
            "name": place.get("display_name", "Hospital"),
            "lat": place.get("lat"),
            "lon": place.get("lon"),
        })

    if not hospitals:
        return jsonify({"error": True})

    return jsonify({"error": False, "data": hospitals})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
