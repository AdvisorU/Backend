from rest_framework.views import APIView
from django.http.response import JsonResponse

from Backend.utils.check_param import check_params
from Backend.models.chat_model import Chat

class Handler(APIView):
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
