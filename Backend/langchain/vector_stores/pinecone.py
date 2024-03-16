from dotenv import load_dotenv
load_dotenv()
import os

from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore

from Backend.langchain import models

pinecone_client = None

def init_pinecone_client():
    return Pinecone(
        api_key = os.getenv('PINECONE_API_KEY'),
    )

def get_index(index_name):
    global pinecone_client

    if pinecone_client is None:
        print('Pinecone client not initialized')
        return None

    return pinecone_client.Index(
        name = index_name
    )

def get_courses_from_catalog_index():
    return get_index(os.getenv('PINECONE_INDEX_COURSES_FROM_CATALOG'))

def get_plan_of_study_index():
    return get_index(os.getenv('PINECONE_INDEX_PLAN_OF_STUDY'))

def get_store(index):
    embedding_client = models.embedding_client

    if embedding_client is None:
        print('Embedding client not initialized')
        return None

    return PineconeVectorStore(
        pinecone_api_key = "fa9a820d-6a64-4876-a8fb-51d3714075a0", 
        embedding = embedding_client,
        index = index
    )

def get_retriever(index):
    return get_store(index).as_retriever()
