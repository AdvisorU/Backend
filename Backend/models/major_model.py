from django.db import models

from .base_model import BaseModel

class Major(BaseModel):
    name = models.CharField(max_length = 255, db_index = True)
    short_name = models.CharField(max_length = 255, db_index = True)
    description = models.TextField()
    parent_major = models.ForeignKey('Major', on_delete = models.CASCADE, related_name = 'major_parent_major', null = True, db_index = True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'short_name': self.short_name,
        }
