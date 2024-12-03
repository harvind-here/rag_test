# from langchain_community.vectorstores import Qdrant
import os
from dotenv import load_dotenv
from langchain_qdrant import Qdrant
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from qdrant_client import QdrantClient
from groq import Groq
load_dotenv()

model_name = "BAAI/bge-base-en"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
embeddings = HuggingFaceBgeEmbeddings(model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs)
print("embedding model loaded")

url = "http://localhost:6333/"
collection_name = 'rag_db'

client = QdrantClient(url=url, prefer_grpc=False)
db = Qdrant(client=client, embeddings=embeddings, collection_name= collection_name)
# print(f"{db}\n\n\n\n")
query = input("Enter the query: ")
docs = db.similarity_search(query=query, k=5)

# for i in docs:
#     doc, score = i
#     print({'score': score, 'content': doc.page_content, "metadata": doc.metadata})

#groq
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
groq_client = Groq(api_key=GROQ_API_KEY)

system_message = f"""you are virtual assistant who helps in summarizing and answering the queries related to the documents uploaded by the user. So the top most similar content from the document is given in the following use that to answer the user's query accurately. The context is as follows: {docs}"""
messages = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": query}
]

response = groq_client.chat.completions.create(
            messages=messages,
            model="llama-3.1-70b-versatile",
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            stop=None,
            stream=False
)

assistant_message = response.choices[0].message
content = assistant_message.content
print("assistant message:", assistant_message)
print("\n\n\n\n\n\n\n")
print("content", content)