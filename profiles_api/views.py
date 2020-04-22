from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""
    def get(self, request, format=None):
        """Returns a list of API view features"""
        an_apiview = [
            'Uses HTTP methods as functions such as (get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Gives most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'hello','an_apiview':an_apiview})