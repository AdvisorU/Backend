import json

from langchain.memory import ConversationBufferMemory

from Backend.models.chat_model import ChatCommentType

def create_memory(histories):
    memory = ConversationBufferMemory()
    
    for history in histories:
        if history.role == ChatCommentType.USER:
            memory.chat_memory.add_user_message(json.dumps({'msg': history.content}))
        elif history.role == ChatCommentType.ASSISTANT:
            memory.chat_memory.add_ai_message(json.dumps({'msg': history.content, 'data': history.extra}))
        else:
            print('Unknown history type:', history.role)
    
    return memory

