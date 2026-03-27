# To import the OpenAI class from langchain_openai
from langchain_openai import OpenAI
from dotenv import load_dotenv

# To load environment variables from .env file
load_dotenv()

# Initialize the OpenAI LLM with a specific model
llm = OpenAI(model_name="gpt-3.5-turbo-instruct")

# Invoke the LLM with a prompt which returns a string response
result = llm.invoke("What is capital of india?")

print(result)