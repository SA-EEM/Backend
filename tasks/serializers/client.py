from rest_framework import serializers
#Modelo
from tasks.models.models import Client
#Serializador Village
from .catalogs import IdentificationTypeSerializer

class GETClientSerializer(serializers.ModelSerializer):
    identification = IdentificationTypeSerializer(many=False, read_only=True)
    
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'middle_name',
                   'third_name', 'first_lastname', 'second_lastname',
                    'married_name', 'nit','email', 'phone_number', 'identification',
                    'insert_date','update_date']
        read_only_fields = ['insert_date']
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['identification'] =IdentificationTypeSerializer(instance.identification).data
        data['insert_date'] = instance.insert_date.strftime('%Y-%m-%d')
        data['update_date'] = instance.update_date.strftime('%Y-%m-%d') if instance.update_date is not None else instance.update_date
        return data
    

class POSTClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'middle_name',
                   'third_name', 'first_lastname', 'second_lastname',
                    'married_name', 'nit','email', 'phone_number', 'identification',
                    'insert_date','update_date']
        read_only_fields = ['insert_date']

