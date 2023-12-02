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

# Similarity search
def get_response_from_query(db, query, k=4):
  # text-davinci max token is 4097

  docs = db.similarity_search(query, k=k)
  docs_content = ''.join([doc.page_content for doc in docs])

  llm = OpenAI(model= "text-davinci-003")

  prompt= PromptTemplate(
    input_variables=["user_query", "docs"],
    template="""
    You are a helpful assistant that can answer questions about youtube videos based on the video's transcript.

    Answer the following question: {user_query}
    By searching the following video transcript: {docs}

    Only use the factual information from the transcript to answer the question.

    If you feel like you don't have enough information to answer the question, say "I don't know, Please ask another question".

    Your answers should be very detailed.
    """,
  )

# create and run our chain
  chain = LLMChain(llm=llm, prompt=prompt)
  response = chain.run(user_query=query, docs=docs_content)
  response = response.replace("\n", "")
  return response, docs


if __name__ == "__main__":
  print(create_vector_db(video_url))

