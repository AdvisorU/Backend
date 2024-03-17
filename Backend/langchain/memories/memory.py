from langchain.memory import ConversationBufferMemory

from Backend.models.chat_model import ChatCommentType

def create_memory(histories):
    memory = ConversationBufferMemory()
    
    for history in histories:
        if history.role == ChatCommentType.USER:
            memory.chat_memory.add_user_message(history.content)
        elif history.role == ChatCommentType.ASSISTANT:
            memory.chat_memory.add_ai_message(history.content)
        else:
            print('Unknown history type:', history.role)
    
    return memory

