import os
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_core.prompts import  ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_community.document_loaders import  PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore

import streamlit as st

load_dotenv()

embeddings = OpenAIEmbeddings()
uploaded_path = "pdf/"
db_store = InMemoryVectorStore(embeddings)
Groqllm = ChatGroq()
def save_file(uploaded_file):
    file_path = uploaded_path + uploaded_file.name
    with open(file_path,"wb") as file:
        file.write(uploaded_file.getbuffer())
    return file_path

def loader(file_path):
    document_loader = PDFPlumberLoader(file_path)
    return document_loader.load()

def getChunks(documents):
    textSplitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
    
    )   
    return textSplitter.split_documents(documents)

def getIndex(chunks):
    return db_store.add_documents(chunks)   

def getDocuments(query):
    return db_store.similarity_search(query)

def generateanswer(query,documents):

    context = "\n".join([doc.page_content for doc in documents]) 
    promptTemplate = ChatPromptTemplate.from_template("""You are a helpful bot that answers quesitons only based on the context
                                                  <context>
                                                  {context}
                                                  </context>
                                                  Question:{input}
                                                  """
    )
    response_chain = promptTemplate| Groqllm | StrOutputParser()
    return response_chain.invoke({"context":context,"input":query})

st.title("PDF RAG Chatbot")
st.markdown("Upload your pdf file from the sidebar. After it is done processing ask your questions on the chatbox below.")

with st.sidebar:
    uploaded = st.file_uploader(
        "Upload your PDF file below:",
        type="pdf",
        help="select a pdf for help",
        accept_multiple_files=False
                                
                                )

    if uploaded:
        saved_path=save_file(uploaded)
        raw = loader(saved_path)
        chunks = getChunks(raw)
        getIndex(chunks)
        st.success("Document processed") 
input = st.chat_input("Enter question below")
if input:
        with st.chat_message("user"):
            st.write(input)
        with st.spinner("analyzing"):
            relevant_docs = getDocuments(input)
            response  = generateanswer(input,relevant_docs)
        with st.chat_message("assistant"):
            st.write(response)


