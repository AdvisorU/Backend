from django.contrib.auth import get_user_model
from django.http.response import JsonResponse
from django.utils import timezone
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from Backend.utils import jwt_auth

from datetime import datetime, timedelta

User = get_user_model()

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.jwt_auth = JWTTokenUserAuthentication()

    def __call__(self, request):
        # 鉴权白名单接口
        if request.path in [
            '/user/register', 
            '/user/login',
            '/user/forget',
            '/user/sms',
        ]:
            return self.get_response(request)

        # 从 Cookie 中获取 JWT
        jwt_token = request.COOKIES.get('SessionID')

        # 使用 JWT 验证登录态
        if jwt_token:
            request.META['HTTP_AUTHORIZATION'] = f'SessionID {jwt_token}'
            token_user, jwt_info = self.jwt_auth.authenticate(request)

            if token_user is not None:
                # 鉴权成功
                user = User.objects.get(id = token_user.id)
                user.last_login = timezone.now()
                user.save()

                request.user = user
                expiry_datetime = datetime.fromtimestamp(jwt_info['exp'])

                # 计算 JWT Token 的有效期是否少于 13 天
                if expiry_datetime - timedelta(days = 13) < datetime.now():
                    # 生成新的 JWT Token
                    new_jwt_token = jwt_auth.gen_jwt_token(user)
                    response = self.get_response(request)
                    response.set_cookie('SessionID', new_jwt_token, expires = jwt_auth.get_cookie_expiretime(), httponly = True, secure = True, samesite = 'Lax')

                    return response

                return self.get_response(request)

        # 未通过登录态验证，返回未授权的响应
        return JsonResponse({
            'code': 401, 
            'msg': 'Unauthorized',
            'data': None, 
        }, status = 401)
