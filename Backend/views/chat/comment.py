from rest_framework.views import APIView
from django.http.response import JsonResponse

from Backend.utils.check_param import check_params
from Backend.models.chat_model import Chat, ChatComment, ChatCommentType
import json
from Backend.langchain.agents import agent
from Backend.langchain.memories import memory
from langchain.prompts import PromptTemplate

class Handler(APIView):
    @check_params({
        'id': {
            'type': 'int',
        }, 
        'offset': {
            'required': False,
            'type': 'int',
            'default': 0, 
            'min': 0,
        },
        'limit': {
            'required': False, 
            'type': 'int',
            'default': 10, 
            'min': 1,
            'max': 100,
        }
    })
    def get(self, request, params):
        chat = Chat.objects.filter(id = params['id']).first()
        
        # check if chat exists
        if not chat:
            return JsonResponse({
                'code': 1, 
                'message': 'Chat not found', 
                'data': None, 
            })
        
        chat_comments = ChatComment.objects.filter(chat = chat).order_by('-created_at')[params['offset']:params['offset'] + params['limit']]
        return JsonResponse({
            'code': 0, 
            'message': 'Chat comments found',
            'data': [
                chat_comment.to_dict()
                for chat_comment in chat_comments
            ], 
        })

    @check_params({
        'id': {
            'type': 'int',
        }, 
        'content': {}
    })
    def post(self, request, params):
        chat = Chat.objects.filter(id = params['id']).first()
        
        # check if chat exists
        if not chat:
            return JsonResponse({
                'code': 1, 
                'message': 'Chat not found', 
                'data': None, 
            })
            
        chat_comments = ChatComment.objects.filter(chat = chat).order_by('created_at')
        
        history = memory.create_memory(chat_comments)
        
        template = '''You are a computer science academic advisor of a university. Answer the following questions about course selection from students as best you can. You can have multiple chat with the student. 

            As an advisor you should know that there usually are:
            - 4 years of college
            - 4 semesters per year, fall (4 classes), spring (4 classes), and summer 1 (2 classes) and summer 2 (2 classes)

            You have access to the following tools:
            {tools}
            - plan-of-study is used when you want to know when a student that's majoring in computer science should take a course.
            - course_from_catalog is used when you want to search for alternative courses for plan-of-study.

            Use the following format, you can skip some of steps if you cannot finish your mission with the information you currently have:
            "Question": "the input question you must answer",
            "Thought": "you should always think about what to do",
            "Action": "don't ask more questions, assume from the query given. for the action to take, should be one of [{tool_names}]",
            "Action Input": "the input to the action",
            "Observation": "the result of the action",
            ... (this Thought/Action/Action Input/Observation can repeat 5 times)
            "Thought": "I now know the final answer",
            "Final Answer": "in json format"

            The answer should be in compact json format, including following fields:
            - msg: your final answer
            - data: the data in an array you used to get the answer
                - 0
                    - major: the major of the course
                    - number: the number of the course
                - 1
                ...
                
            If the user says something not related to your job as an academic advisor, return a message that explain you cannot answer the question. 

            Begin!

            Question: {input}
            Thought:{agent_scratchpad}'''
        
        prompt = PromptTemplate.from_template(template)
        
        agent_executer = agent.create_agent(memory = history, prompt = prompt)
        
        agent_executer.invoke(input = {
            'input': params['content'],
        })
        
        ChatComment.objects.create(
            chat = chat,
            user = request.user,
            role = ChatCommentType.USER,
            content = params['content'],
        )
        
        content = json.loads(history.chat_memory.messages[-1].content)
        msg = content['msg']
        data = None
        if 'data' in content:
            data = content['data']
        
        ChatComment.objects.create(
            chat = chat,
            role = ChatCommentType.ASSISTANT,
            content = msg, 
            extra = data,
        )
        
        return JsonResponse({
            'code': 0, 
            'message': 'Chat comment created', 
            'data': {
                'msg': msg, 
                'data': data,
            }
        })
