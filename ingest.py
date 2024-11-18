from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load and split the PDF
loader = PyPDFLoader(file_path="./pdfs")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=100)
chunks = text_splitter.split_documents(docs)

# Create and save the FAISS vector store
embedding = HuggingFaceEmbeddings( )
vector_store = FAISS.from_documents(documents=chunks, embedding=embedding)
vector_store.save_local("faiss_index")
