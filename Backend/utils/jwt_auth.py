from rest_framework_simplejwt.tokens import AccessToken
import datetime

jwt_token_lifetime = 14

def gen_jwt_token(user):
    jwt_token = AccessToken.for_user(user)
    jwt_token.set_exp(lifetime = datetime.timedelta(days = jwt_token_lifetime))  # 设置 token 的有效期
    return str(jwt_token)

def get_cookie_expiretime():
    expires_date = datetime.datetime.now() + datetime.timedelta(days = jwt_token_lifetime)
    return expires_date.strftime("%a, %d %b %Y %H:%M:%S GMT")
