from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_community.document_loaders import YoutubeLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from dotenv import load_dotenv
import os


load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'This is a Chrome extension for summarising YouTube Videos simply by inputting the video URL!'



@app.route('/summary', methods=['GET'])
def generateSummary():
    inputURL = request.args.get('inputURL')
    # inputURL = str(inputURL)
    print(inputURL)

    loader = YoutubeLoader.from_youtube_url(inputURL, add_video_info=False)
    docs = loader.load()
    
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    text_splitter = RecursiveCharacterTextSplitter()
    documents = text_splitter.split_documents(docs)
    vector = FAISS.from_documents(documents, embeddings)
    print(documents)

    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:
    <context>
    {context}
    </context>
    Question: {input}""")

    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = vector.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    response = retrieval_chain.invoke({"input": "What is the video about, tell me about it in high details"})
    print(response["answer"])

    return jsonify({'summary': response["answer"]})



if __name__ == '__main__':
    app.run(port=8000, debug=False) # In Mac, always use port other than 5000 or 7000, port is use for control centre


# Initilize backend: flask run --port=8000 | python3 app.py