from dotenv import load_dotenv
load_dotenv()
import os

from langchain_openai import AzureChatOpenAI

def init_chat_client():
    return AzureChatOpenAI(
        azure_endpoint = os.getenv('OPENAI_AZURE_HOST'),
        api_key = os.getenv('OPENAI_API_KEY'),
        api_version = os.getenv('OPENAI_API_VERSION'),
        model = os.getenv('OPENAI_GPT35_MODEL'), 
        temperature = 0,
    )
