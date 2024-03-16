from django.db import models

from .base_model import BaseModel

class Chat(BaseModel):
    title = models.CharField(max_length = 255, null = True, db_index = True)
    user = models.ForeignKey('User', on_delete = models.CASCADE, related_name = 'chat_user', db_index = True)
    comment_count = models.IntegerField(default = 0)

class ChatCommentType(models.TextChoices):
    SYSTEM = 'SYSTEM', 'SYSTEM'
    USER = 'USER', 'USER'
    ASSISTANT = 'ASSISTANT', 'ASSISTANT'

class ChatComment(BaseModel):
    chat = models.ForeignKey('Chat', on_delete = models.CASCADE, related_name = 'chat_comment_chat', db_index = True)
    user = models.ForeignKey('User', on_delete = models.CASCADE, related_name = 'chat_comment_user', null = True, db_index = True)
    role = models.CharField(max_length = 255, choices = ChatCommentType.choices, db_index = True)
    visibility = models.BooleanField(default = True, db_index = True)
    content = models.TextField()
    extra = models.JSONField(null = True)
