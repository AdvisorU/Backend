from rest_framework.views import APIView
from django.http.response import JsonResponse

from django.db.models import Q

from Backend.utils.check_param import check_params
from Backend.models.course_model import Course

class Handler(APIView):
    @check_params({
        'major': {}, 
        'offset': {
            'required': False, 
            'type': 'int',
            'default': 0, 
            'min': 0,
        },
        'limit': {
            'required': False, 
            'type': 'int',
            'default': 10, 
            'min': 1,
            'max': 100,
        }
    })
    def get(self, request, params):
        # search course by given conditions
        query = Q(major=params['major'])
        
        # search course by given conditions
        courses = Course.objects.filter(query)[params['offset']:params['offset']+params['limit']]
        courses = [
            {
                'id': course.id,
                'major': course.major,
                'number': course.number,
                'name': course.name,
                'description': course.description,
                'credit_hours': course.credit_hours,
            }
            for course in courses
        ]

        return JsonResponse({
            'code': 0, 
            'message': 'Courses found',
            'data': courses,
        })
