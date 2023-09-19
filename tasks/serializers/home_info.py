from rest_framework import serializers
#Modelo
from tasks.models.models import HomeInformation
from tasks.models.models import Village
#Serializador Village
from .catalogs import VillageSerializer

class GETHomeInformationSerializer(serializers.ModelSerializer):
    id_village = VillageSerializer(many=False)
    
    class Meta:
        model = HomeInformation
        fields = ['id', 'municipality_name', 'addres', 'zone_number', 'reference', 'id_village', 'insert_date', 'update_date']
        read_only_fields = ['insert_date']
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['id_village'] = VillageSerializer(instance.id_village).data
        data['insert_date'] = instance.insert_date.strftime('%Y-%m-%d')
        data['update_date'] = instance.update_date.strftime('%Y-%m-%d') if instance.update_date is not None else instance.update_date
        return data
    

class POSTHomeInformationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HomeInformation
        fields = ['id', 'municipality_name', 'addres', 'zone_number', 'reference', 'id_village', 'insert_date', 'update_date']
        read_only_fields = ['insert_date']

