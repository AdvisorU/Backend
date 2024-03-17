from rest_framework.views import APIView
from django.http.response import JsonResponse

from django.db.models import Q

from Backend.utils.check_param import check_params
from Backend.models.course_model import Course
from Backend.models.major_model import Major

class Handler(APIView):
    @check_params({
        'major': {
            'required': False, 
        }, 
        'keywords': {
            'required': False,
        }, 
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
        query = Q()

        if 'major' in params:
            major = Major.objects.filter(short_name = params['major']).first()

            # check if major exists
            if not major:
                return JsonResponse({
                    'code': 1, 
                    'message': 'Major not found', 
                    'data': None, 
                })
            
            query &= Q(major = major)

        if 'keywords' in params:
            query &= Q(keywords__contains = params['keywords'])
        
        # search course by given conditions
        courses = Course.objects.filter(query)[params['offset']:params['offset']+params['limit']]
        courses = [
            course.to_dict()
            for course in courses
        ]

        return JsonResponse({
            'code': 0, 
            'message': 'Courses found',
            'data': courses,
        })
