from dotenv import load_dotenv
load_dotenv()
import os

from langchain_openai import AzureOpenAIEmbeddings

def init_embedding_client():
    return AzureOpenAIEmbeddings(
        azure_endpoint = os.getenv('OPENAI_AZURE_HOST'),
        api_key = os.getenv('OPENAI_API_KEY'),
        api_version = os.getenv('OPENAI_API_VERSION'),
        model = os.getenv('OPENAI_EMBEDDING_MODEL')
    )
