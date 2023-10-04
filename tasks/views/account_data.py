from rest_framework import viewsets
#Modelo
from tasks.models.models import AccountData
#Serializer
from tasks.serializers.account_data import GETAccountDataSerializer, POSTAccountDataSerializer

class AccountDataViewSet(viewsets.ModelViewSet):
    queryset = AccountData.objects.all()
    serializer_class = GETAccountDataSerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return GETAccountDataSerializer
        else:
            return POSTAccountDataSerializer