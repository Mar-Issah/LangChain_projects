from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
# to use the langchain agents import below the ff
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.agents import load_tools
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

  name_chain = LLMChain(llm = llm, prompt = prompt_template, output_key= 'pet_names')
  response = name_chain({'animal_type': animal_type, 'animal_color':animal_color})

  # response will be the output of the llmchain
  return response

def langchain_agent():
  llm = OpenAI(temperature=0.5)

  #  Initializing the agent
  tools = load_tools(['wikipedia', 'llm-math'],llm=llm)
  agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

  #Running the agent
  result = agent.run('What is the average age of a dog? Multiply the age by 3')
  print(result)

if __name__ == "__main__":
  print(generate_name("cow",'brown'))
  # langchain_agent()
