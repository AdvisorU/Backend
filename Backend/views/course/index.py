from rest_framework.views import APIView
from django.http.response import JsonResponse

from Backend.utils.check_param import check_params
from Backend.models.course_model import Course

class Handler(APIView):
    @check_params({
        'id': {}
    })
    def get(self, request, params):
        # find course by id
        course = Course.objects.get(id=params['id'])

        if course:
            course_data = course.to_dict()

            # find course's NUPathAttributes
            course_nu_path_attributes = course.course_nu_path_attributes_course.all()
            course_data['nu_path_attributes'] = [
                {
                    'id': course_nu_path_attribute.id,
                    'name': course_nu_path_attribute.attribute.name,
                    'description': course_nu_path_attribute.attribute.description,
                }
                for course_nu_path_attribute in course_nu_path_attributes
            ]

            # find course's co-requisites
            course_co_requisites = course.course_co_requisites_course.all()
            course_data['co_requisites'] = [
                course_co_requisite.to_dict()
                for course_co_requisite in course_co_requisites
            ]

            # find course's pre-requisites
            course_pre_requisites = course.course_pre_requisites_course.all()
            course_data['pre_requisites'] = [
                course_pre_requisite.to_dict()
                for course_pre_requisite in course_pre_requisites
            ]

            return JsonResponse({
                'code': 0, 
                'message': 'Course found',
                'data': course_data, 
            })
        else:
            return JsonResponse({
                'code': 1, 
                'message': 'Course not found', 
                'data': None, 
            })
