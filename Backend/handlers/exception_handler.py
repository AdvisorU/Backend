from rest_framework.views import exception_handler
from django.http.response import JsonResponse

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        # Customize the error message format
        customized_data = {
            'status': 1, 
            'msg': response.data.get('detail', 'Internal Server Error'), 
        }
        response.data = customized_data

    return response
