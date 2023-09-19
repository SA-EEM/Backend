from rest_framework import viewsets
#Modelo
from tasks.models.models import HomeInformation
#Serializer
from tasks.serializers.home_info import GETHomeInformationSerializer, POSTHomeInformationSerializer

class HomeInfoViewSet(viewsets.ModelViewSet):
    queryset = HomeInformation.objects.all()
    serializer_class = GETHomeInformationSerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return GETHomeInformationSerializer
        else:
            return POSTHomeInformationSerializer