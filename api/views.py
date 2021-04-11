# INTERNAL MODULES
from django.shortcuts import render

# EXTERNAL MODULES
from rest_framework.views import APIView,Response
from rest_framework.reverse import reverse

# LOCAL MODULES


# Create your views here.
class RootAPI(APIView):
    def get(self, request):
        data = {
            'Blog': reverse('api:blog', request=request),
        }
        return Response(data)