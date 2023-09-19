from rest_framework import viewsets
#Modelo
from tasks.models.models import Client
#Serializer
from tasks.serializers.client import GETClientSerializer, POSTClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = GETClientSerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return GETClientSerializer
        else:
            return POSTClientSerializer