from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
#docker run -p 6333:6333 -v .:/qdrant/storage qdrant/qdrant

loader  = PyPDFLoader("Attention.pdf")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
texts = text_splitter.split_documents(documents)

#embedding model load
model_name = "BAAI/bge-base-en"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
embeddings = HuggingFaceBgeEmbeddings(model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs)
print("embedding model loaded")

url = "http://localhost:6333/"
collection_name = 'rag_db'

#qdrant
qdrant = Qdrant.from_documents(texts, embeddings, url=url, prefer_grpc = False, collection_name=collection_name)



