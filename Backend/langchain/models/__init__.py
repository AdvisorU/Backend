from . import chatbots, embeddings

chatbot_client = None
embedding_client = None

def init():
    global chatbot_client
    chatbot_client = chatbots.init_chat_client()
    global embedding_client
    embedding_client = embeddings.init_embedding_client()
