from django.urls import path

from . import index, comment, list

urlpatterns = [
    path('', index.Handler.as_view()),
    path('comment/', comment.Handler.as_view()),
    path('list/', list.Handler.as_view()),
]
