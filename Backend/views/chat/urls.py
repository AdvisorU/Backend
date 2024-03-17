from django.urls import path

from . import index, list

urlpatterns = [
    path('', index.Handler.as_view()),
    path('list/', list.Handler.as_view()),
]
