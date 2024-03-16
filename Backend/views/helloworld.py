from rest_framework.views import APIView
from django.http.response import JsonResponse

from Backend.utils.check_param import check_params

class Handler(APIView):
    @check_params({
        'msg': {
            'required': False, 
        }, 
    })
    def get(self, request, params):
        return JsonResponse({
            'status': 0, 
            'msg': '你好世界' + (', {}'.format(params['msg']) if 'msg' in params else ''), 
            'data': {
                'user_id': request.user.id, 
            }, 
        })
