from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = "gpt-4", temperature=1.8, max_completion_tokens=50)
response = model.invoke("Describe the theory of relativity in simple terms.")
print(response.content)