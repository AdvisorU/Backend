from django.db import models

from Backend.utils.snowflake import generate_uid

class BaseModel(models.Model):
    id = models.BigIntegerField(primary_key = True, default = generate_uid, editable = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True
