import os

os.environ["OPENAI_API_KEY"] = "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"
# pip install pypdf to be able to inject pdf in python
#this time we are loading a pdf document not a .txt doc so we use the PyPDFLoader to load the document and read/split it into chunks
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI



if __name__ == "__main__":
    print("Chat with my PDF!")
    pdf_path = "C:/MARSIYA/PROGRAMMING/PORTFORLIO/ALL NOTES/AI/LANGCHAIN/LangChain_projects/Chat_with_pdf/sample.pdf"
    loader = PyPDFLoader(file_path=pdf_path)
    documents = loader.load()
    print(documents)

	#initailize the text splitter
    text_splitter = CharacterTextSplitter(
        chunk_size=1000, chunk_overlap=30, separator="\n"
    )
    # split the document into chunks
    docs = text_splitter.split_documents(documents=documents)