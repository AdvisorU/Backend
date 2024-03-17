from rest_framework.views import APIView
from django.http.response import JsonResponse

from django.db.models import Q

from Backend.utils.check_param import check_params
from Backend.models.chat_model import Chat

class Handler(APIView):
    @check_params({
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
        chats = Chat.objects.filter(user = request.user).order_by('-updated_at')[params['offset']:params['offset']+params['limit']]
        
        return JsonResponse({
            'code': 0, 
            'message': 'Success', 
            'data': [chat.to_dict() for chat in chats], 
        })
