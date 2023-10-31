from django.utils import timezone
from rest_framework import serializers
#Modelo
from tasks.models.models import HomeInformation
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
    
    def update(self, instance, validated_data):
        update_fields = []
        for field in ['municipality_name', 'addres', 'zone_number', 'reference', 'id_village', 'update_date']:
            if field in validated_data:
                setattr(instance, field, validated_data[field])
                update_fields.append(field)
        
        if update_fields:
            instance.update_date = timezone.now()
            instance.save(update_fields=update_fields)
        
        return instance
