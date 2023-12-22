import os
from langchain.document_loaders import PyMuPDFLoader, PyPDFDirectoryLoader
from langchain.embeddings import VoyageEmbeddings, OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import DeepLake
from dotenv import load_dotenv
load_dotenv()

embeddings = VoyageEmbeddings(model="voyage-lite-01", show_progress_bar=True)

def init_vectorstore(dataset_path="hub://p1utoze/default", embeddings="voyage/voyage-lite-01"):
    db = DeepLake(dataset_path=dataset_path, embedding=embeddings)
    return db

def load_documents(base_path="data/INFORMATION-TECHNOLOGY/"):
    for file in os.listdir(base_path):
        path = base_path + file
        print(path)
        loader = PyMuPDFLoader(path)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=50)
    docs = loader.load_and_split(text_splitter)
    db = init_vectorstore("hub://p1utoze/resumes", embeddings)
    db.add_documents(docs)


# print(load_documents())