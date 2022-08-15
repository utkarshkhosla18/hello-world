from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from . import models


class Authtication(BaseAuthentication):

    def authenticate(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION', None)
        except:
            raise exceptions.AuthenticationFailed('Authentication failed')
        token = token.split(' ')[1]
        print(token)
        token_query = models.UserToken.objects.filter(token=token)
        if not token_query:
            raise exceptions.AuthenticationFailed('invalid token')
        # 返回（当前登录对象，token）
        return token_query.first().user, token_query.first()

    def authenticate_header(self, request):
        return 'Basic realm="user"'
