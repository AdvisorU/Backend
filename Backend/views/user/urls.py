from django.urls import path

from . import login, info

urlpatterns = [
    path('login', login.Handler.as_view()),
    path('info', info.Handler.as_view()),
]
