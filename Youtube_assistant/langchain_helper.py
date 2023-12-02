from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()

#initialzie the openaiembeddings
embeddings_model = OpenAIEmbeddings()

# video to create vector db from
video_url = 'https://www.youtube.com/watch?v=-8Yu2GiuSns'

def create_vector_db(video_url : str) -> FAISS:
  # first load the video using YoutubeLoader
  loader = YoutubeLoader.from_youtube_url(video_url)
  transcript = loader.load()

  # split transcript into chunk
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=100)
  docs = text_splitter.split_documents(transcript)

  # save in our vector store
  db = FAISS.from_documents(docs, OpenAIEmbeddings())
  return db


if __name__ == "__main__":
  print(create_vector_db(video_url))

