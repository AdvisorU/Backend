from rest_framework.views import APIView
from django.http.response import JsonResponse

from Backend.utils.check_param import check_params
from Backend.models.chat_model import Chat, ChatComment, ChatCommentType

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
        chat = Chat.objects.create(
            title = 'New chat',
            user = request.user,
        )
        return JsonResponse({
            'code': 0, 
            'message': 'Chat created',
            'data': chat.to_dict(), 
        })
