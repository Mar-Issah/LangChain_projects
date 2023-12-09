import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    print("Chat with my PDF!")
    pdf_path = "C:/MARSIYA/PROGRAMMING/PORTFORLIO/ALL NOTES/AI/LANGCHAIN/LangChain_projects/Chat_with_pdf/sample.pdf"
    loader = PyPDFLoader(file_path=pdf_path)
    documents = loader.load()

	#initailize the text splitter
    text_splitter = CharacterTextSplitter(
        chunk_size=1000, chunk_overlap=30, separator="\n"
    )
    # split the document into chunks
    docs = text_splitter.split_documents(documents=documents)

  # Initialize the openai embeddings and vector db. We are using a local vector store called FAISS
    embeddings = OpenAIEmbeddings()

    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("faiss_index_react")

    new_vectorstore = FAISS.load_local("faiss_index_react", embeddings)
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(), chain_type="stuff", retriever=new_vectorstore.as_retriever()
    )
    res = qa.run("In one sentence what is ReAct?")
    print(res)