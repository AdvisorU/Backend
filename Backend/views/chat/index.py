from rest_framework.views import APIView
from django.http.response import JsonResponse

from Backend.utils.check_param import check_params
from Backend.models.chat_model import Chat

class Handler(APIView):
    @check_params({
        'id': {
            'type': 'int',
        },
    })
    def get(self, request, params):
        chats = Chat.objects.filter(user = request.user).first()
        
        if not chats:
            return JsonResponse({
                'code': 1, 
                'message': 'Chats not found', 
                'data': None, 
            })
            
        return JsonResponse({
            'code': 0, 
            'message': 'Chats found',
            'data': chats.to_dict(),
        })
    
    @check_params({})
    def post(self, request, params):
        chat = Chat.objects.create(
            title = None,
            user = request.user,
        )
        return JsonResponse({
            'code': 0, 
            'message': 'Chat created',
            'data': chat.to_dict(), 
        })
