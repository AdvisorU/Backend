from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from Backend.utils.snowflake import generate_uid

class UserManager(BaseUserManager):
    def create_user(self, email = None, password = None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email) if email else None

        user = self.model(
            email = email,
            **extra_fields
        )
        user.nickname = 'User ' + str(user.id)
        user.set_password(password)
        user.save(using=self._db)

        return user

class User(AbstractBaseUser):
    id = models.BigIntegerField(primary_key = True, default = generate_uid, editable = False)
    email = models.EmailField(unique = True, max_length = 75, blank = True, null = True)
    password = models.CharField(max_length=128)
    nickname = models.TextField(default = 'User')
    icon = models.TextField(blank = True, null = True)
    registration_time = models.DateTimeField(auto_now_add = True)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['phone']

    objects = UserManager()

    def __str__(self):
        return str(self.id)
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'email': self.email,
            'nickname': self.nickname,
            'icon': self.icon,
            'registration_time': self.registration_time,
        }
