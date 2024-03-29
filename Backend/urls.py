from django.urls import include, path

from .views import helloworld
from .views.course import urls as course_urls
from .views.user import urls as user_urls
from .views.chat import urls as chat_urls

urlpatterns = [
    path('course/', include(course_urls)),
    path('user/', include(user_urls)),
    path('helloworld', helloworld.Handler.as_view()),
    path('chat/', include(chat_urls)),
]
