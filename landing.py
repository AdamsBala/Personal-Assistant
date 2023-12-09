from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from flask import Blueprint, render_template, request, jsonify

landing = Blueprint(__name__, "landing")
loader = DirectoryLoader("./data", glob="*.txt")
index = VectorstoreIndexCreator().from_loaders([loader])


@landing.route("/")
def home():
    return render_template("index.html")


@landing.route("/query", methods=['POST'])
def get_data():
    query = request.json['messages'][-1]['content']
    data = index.query(query)
    return jsonify({"completion": data})
