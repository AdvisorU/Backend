from django.db.models import Q
from django.utils import timezone
from rest_framework.views import APIView
from django.http.response import JsonResponse

from Backend.utils.check_param import check_params
from Backend.utils import jwt_auth
from Backend.models import user_model

class Handler(APIView):
    @check_params({
        'type': {
            're': r'^[01]$',
            'type': 'int', 
        }, 
        'email': {
            're': r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$',
            'required': False, 
        },
        'password': {
            're': r'^.{8,}$',
            'required': False, 
        }, 
    })
    def post(self, request, params):
        user = None

        if params['type'] == 0:
            user = user_model.User.objects.filter(email = params['email']).first()
            verified = user and user.check_password(params['password'])
            err_msg = 'Wrong email or password'

        if verified:
            user.last_login = timezone.now()
            user.save()

            # 用户验证通过，生成 JWT
            jwt_token = jwt_auth.gen_jwt_token(user)

            # 将 JWT 设置到 Cookie 中
            response = JsonResponse({
                'status': 0,
                'msg': 'Login success',
                'data': None,
            })
            response.set_cookie('SessionID', jwt_token, expires = jwt_auth.get_cookie_expiretime(), httponly = True, secure = True, samesite = 'Lax')

            return response

        return JsonResponse({
            'status': 1, 
            'msg': err_msg, 
            'data': None, 
        })
