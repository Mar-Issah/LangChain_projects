import os

from langchain.document_loaders import TextLoader	#since it is only text from blog site, we are using TextLoader and CharacterTextSplitter
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
# from langchain import VectorDBQA, OpenAI
from langchain.chains import VectorDBQA
from langchain.llms import OpenAI
# RetrivalAQ/VectDBQA: This chain is designed for question-answering tasks where the answer is retrieved from a given context. It's useful when you have a specific document or set of documents that you want to extract information from.
# import pinecone	# pip install pinecone-client
# we are using pinecone vector database https://www.pinecone.io/


if __name__ == "__main__":
    print("Hello VectorStore!")
    loader = TextLoader("C:/MARSIYA/PROGRAMMING/PORTFORLIO/ALL NOTES/AI/LANGCHAIN/LangChain_projects/Document_Assistant/Medium/mediumblog.txt",encoding="utf-8"