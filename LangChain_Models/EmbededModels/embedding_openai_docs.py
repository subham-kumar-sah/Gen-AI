from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)
result = embeddings.embed_documents(["Delhi is the capital of India", "Paris is the capital of France", "Tokyo is the capital of Japan"])
print(str(result))