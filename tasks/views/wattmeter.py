from rest_framework import viewsets
#Modelo
from tasks.models.models import Wattmeter
#Serializer
from tasks.serializers.wattmeter import GETWattmeterSerializer, POSTWattmeterSerializer

class WattmeterViewSet(viewsets.ModelViewSet):
    queryset = Wattmeter.objects.all()
    serializer_class = GETWattmeterSerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return GETWattmeterSerializer
        else:
            return POSTWattmeterSerializer