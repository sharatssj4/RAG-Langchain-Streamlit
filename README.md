Streamlit RAG with LangChain

Overview

This project implements a Retrieval-Augmented Generation (RAG) application using LangChain and Streamlit. It allows users to upload a pdf file and create a knowledge base that retrieves relevant documents before generating responses.

Features

Streamlit UI: Interactive and user-friendly interface.

LangChain Integration: Utilizes LangChain for retrieval and generation.

Vector Database: Stores and retrieves documents efficiently. This uses Inmemory. Plug and play Chromadb and pinecone or whatever you like.

LLM Support: Connects to various language models like OpenAI, Hugging Face, or local LLMs. This uses Groqllm.

Document Upload: Supports uploading PDFs.

Real-time Query Processing: Generates responses dynamically based on retrieved documents.

Installation

Prerequisites

Ensure you have Python 3.8+ installed.

Steps

Clone the repository:

git clone https://github.com/yourusername/streamlit-rag-langchain.git
cd streamlit-rag-langchain

Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

Set up environment variables:

Create a .env file and add the necessary API keys (e.g., OpenAI API key, vector database credentials).

Run the application:

streamlit run app.py

Usage

Upload documents via the Streamlit interface.

Enter queries in the chatbot input field.

Receive responses generated based on retrieved documents.

Deployment

To deploy on a cloud platform, follow these steps:

Deploy to Streamlit Cloud

Push your repository to GitHub.

Go to Streamlit Cloud and link your repository.

Configure environment variables in Streamlit Cloud settings.

Deploy the application.

Docker Deployment

Build and run a Docker container:

docker build -t streamlit-rag .
docker run -p 8501:8501 streamlit-rag

Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

License

This project is licensed under the MIT License.
