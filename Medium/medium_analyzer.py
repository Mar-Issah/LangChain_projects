import os

from langchain.document_loaders import TextLoader	#since it is only text from blog site, we are using TextLoader and CharacterTextSplitter
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
# from langchain import VectorDBQA, OpenAI
from langchain.chains import VectorDBQA
from langchain.llms import OpenAI
import pinecone	# pip install pinecone-client
# we are using pinecone vector database https://www.pinecone.io/

pinecone.init(
    api_key="your_keys_here",
    environment="gcp-starter",
)

if __name__ == "__main__":
    print("Hello VectorStore!")

    # First: load the document
    loader = TextLoader("C:/MARSIYA/PROGRAMMING/PORTFORLIO/ALL NOTES/AI/LANGCHAIN/LangChain_projects/Document_Assistant/Medium/mediumblog.txt",encoding="utf-8")
    document = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(document)

    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))
    docsearch = Pinecone.from_documents(
        texts, embeddings, index_name="medium-blogs-embeddings-index"
    )

    qa = VectorDBQA.from_chain_type(
        llm=OpenAI(openai_api_key=os.environ.get("OPENAI_API_KEY")), chain_type="stuff", vectorstore=docsearch, return_source_documents=True
    )
    query = "What is a vector DB? Give me a 15 word answer for a begginner"
    result = qa({"query": query})
    print(result)

