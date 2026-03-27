from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

documents = ["Virat Kolhi is a great cricketer with aggressive batting style and outstanding performance",
              "Sachin Tendulkar is a legendary cricketer with a remarkable career", 
              "Rohit Sharma is an excellent batsman with a strong track record", 
              "MS Dhoni is a former Indian cricketer known for his calm demeanor and leadership skills"]

query = "Who is MS Dhoni?"

doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0] # Both Should be 2D Array and cosine similarity returns 2D Array

index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print(query)
print(documents[index])
print("Similarity Score:", score)