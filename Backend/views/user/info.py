from rest_framework.views import APIView
from django.http.response import JsonResponse

from Backend.utils.check_param import check_params

import json

class Handler(APIView):
    @check_params({})
    def get(self, request, params):
        return JsonResponse({
            'code': 0, 
            'message': '获取用户信息成功', 
            'data': {
                'id': request.user.id, 
                'nickname': request.user.nickname, 
                'icon': request.user.icon, 
                'email': request.user.email, 
                'last_login': request.user.last_login, 
            }, 
        })
    
    @check_params({
        'nickname': {
            'required': False, 
        }, 
        'icon': {
            'required': False, 
        }, 
        'email': {
            'required': False, 
        }, 
        'password': {
            'required': False, 
        }, 
    })
    def post(self, request, params):
        try:
            if 'nickname' in params:
                request.user.nickname = params['nickname']
                
            if 'icon' in params:
                request.user.icon = params['icon']

            if 'email' in params:
                request.user.email = params['email']

            if 'password' in params:
                request.user.set_password(params['password'])
            
            request.user.save()

            return JsonResponse({
                'code': 0, 
                'message': '用户信息修改成功', 
                'data': None, 
            })
        except Exception as e:
            print(e)
            return JsonResponse({
                'code': 0, 
                'message': '用户信息修改失败：' + str(e), 
                'data': None, 
            })
