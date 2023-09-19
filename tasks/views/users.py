from rest_framework import viewsets
#Modelo
from tasks.models.models import Users
#Serializer
from tasks.serializers.users import GETUsersSerializer, POSTUsersSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = GETUsersSerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return GETUsersSerializer
        else:
            return POSTUsersSerializer