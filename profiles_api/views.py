from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import permissions
from profiles_api import serializers
from profiles_api import models



class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of API view features"""
        an_apiview = [
            'Uses HTTP methods as functions such as (get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Gives most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self,request):
        """ create a hello message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """This handles updating an Object , also this is basically replacing an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Deleting of an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list,create,update,partial-update,retrieve)',
            'Automatically maps URLs using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'method':'Hello!','a_viewset':a_viewset})

    def create(self,request):
        """Create a new Hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """Handles getting an object by its id"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handles updating an object by its id"""
        return Response({'http_method':'UPDATE'})

    def partial_update(self,request,pk=None):
        """Handles updating part of an object by its id"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handles removing an object"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class UserLoginApiView(ObtainAuthToken):
    """Handles creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

