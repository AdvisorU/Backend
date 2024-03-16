from django.utils import timezone
from rest_framework.views import APIView
from django.http.response import JsonResponse

from Backend.utils.check_param import check_params
from Backend.models.major_model import Major

class Handler(APIView):
    @check_params({
        'major': {
            'type': 'int', 
        }, 
        'plan': {
            'type': 'json', 
        },
    })
    def post(self, request, params):
        major = Major.objects.filter(id=params['major'])

        if not major.exists():
            return JsonResponse({
                'code': 1, 
                'message': 'Major not found',
            })
        
        major = major.first()

        # validate the nu path attributes
        

        # validate the pre-requisites


        # validate the co-requisites


        # validate the credit hours
