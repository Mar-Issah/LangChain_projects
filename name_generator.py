from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

def generate_name(animal_type, animal_color):
  # For it to be more accurate you can give a temperature as 0.4 or lesser.
  llm = OpenAI(temperature=0.5)

  prompt_template = PromptTemplate(
    input_variables=['animal_type', 'animal_color'],
    template='I have a {animal_type} pet. It is {animal_color}. Suggest me five cool names'
  )

  name_chain = LLMChain(llm = llm, prompt = prompt_template)
  response = name_chain({'animal_type': animal_type, 'animal_color':animal_color})

  # response will be what the output of the llmchain
  return response

if __name__ == "__main__":
  print(generate_name("cow",'black'))
