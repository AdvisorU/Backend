from django.db import models

from .base_model import BaseModel

class Course(BaseModel):
    major = models.CharField(max_length = 255, db_index = True)
    number = models.CharField(max_length = 255, db_index = True)
    name = models.CharField(max_length = 255, db_index = True)
    description = models.TextField(null = True)
    credit_hours = models.IntegerField(null = True)
    credit_hours_min = models.IntegerField(null = True)
    credit_hours_max = models.IntegerField(null = True)

    def to_dict(self):
        return {
            'id': self.id,
            'major': self.major,
            'number': self.number,
            'name': self.name,
            'description': self.description,
            'credit_hours': self.credit_hours,
            'credit_hours_min': self.credit_hours_min,
            'credit_hours_max': self.credit_hours_max,
        }

class NUPathAttribute(BaseModel):
    name = models.CharField(max_length = 255, db_index = True)
    short_name = models.CharField(max_length = 255, db_index = True)
    user_code = models.CharField(max_length = 255, null = True, db_index = True)
    description = models.TextField(null = True)

class CourseNUPathAttribute(BaseModel):
    course = models.ForeignKey('Course', on_delete = models.CASCADE, related_name = 'course_nu_path_attributes_course', db_index = True)
    attribute = models.ForeignKey('NUPathAttribute', on_delete = models.CASCADE, related_name = 'course_nu_path_attributes_attribute', db_index = True)

class CourseCoRequisite(BaseModel):
    course = models.ForeignKey('Course', on_delete = models.CASCADE, related_name = 'course_co_requisites_course', db_index = True)
    co_requisite = models.ForeignKey('Course', on_delete = models.CASCADE, related_name = 'course_co_requisites_co_requisite', db_index = True)

    def to_dict(self):
        return {
            'id': self.co_requisite.id,
            'major': self.co_requisite.major,
            'number': self.co_requisite.number,
            'name': self.co_requisite.name,
            'description': self.co_requisite.description,
            'credit_hours': self.co_requisite.credit_hours,
        }

class CoursePreRequisiteType(models.TextChoices):
    COURSE = 'COURSE', 'COURSE'
    GROUP = 'GROUP', 'GROUP'

class CoursePreRequisite(BaseModel):
    type = models.CharField(max_length = 255, choices = CoursePreRequisiteType.choices, db_index = True)
    course = models.ForeignKey('Course', on_delete = models.CASCADE, related_name = 'course_pre_requisites_course', null = True, db_index = True)
    parent_pre_requisite = models.ForeignKey('CoursePreRequisite', on_delete = models.CASCADE, related_name = 'course_pre_requisites_parent_pre_requisite', null = True, db_index = True)
    pre_requisite = models.ForeignKey('Course', on_delete = models.CASCADE, related_name = 'course_pre_requisites_pre_requisite', null = True, db_index = True)
    minimum_grade = models.CharField(max_length = 255, null = True)

    def to_dict(self):
        if self.type == CoursePreRequisiteType.COURSE:
            data = self.pre_requisite.to_dict()

            if self.minimum_grade:
                data['minimum_grade'] = self.minimum_grade

            return data
        else:
            data = []

            for pre_requisite in self.course_pre_requisites_parent_pre_requisite.all():
                data.append(pre_requisite.to_dict())

            return data
        
