from rest_framework import viewsets
#Modelo
from tasks.models.models import Users
#Serializer
from tasks.serializers.users import GETUsersSerializer, POSTUsersSerializer

from rest_framework import status
from rest_framework.views import APIView

from django.contrib.auth import authenticate
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = GETUsersSerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return GETUsersSerializer
        else:
            return POSTUsersSerializer
        

class LoginView (APIView):
    permission_classes = []
    
    def post (self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username = username, password = password)
        
        if user:
            return Response(
                {'token': user.auth_token.key}
            )
        else:
            return Response(
                {'error': 'Credenciales inválidas. Inicie sesión.'},
                status= status.HTTP_400_BAD_REQUEST
            )