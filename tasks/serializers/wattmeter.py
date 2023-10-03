from rest_framework import serializers
#Modelo
from tasks.models.models import Wattmeter
#Serializador Wattmeter Brand
from .catalogs import WattmeterBrandSerializer

class GETWattmeterSerializer(serializers.ModelSerializer):
    wattmeter_brand = WattmeterBrandSerializer(many=False)
    
    class Meta:
        model = Wattmeter
        fields = ['id', 'wattmeter_number', 'wattmeter_brand', 'insert_date', 'update_date']
        read_only_fields = ['insert_date']
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['wattmeter_brand'] = WattmeterBrandSerializer(instance.wattmeter_brand).data
        data['insert_date'] = instance.insert_date.strftime('%Y-%m-%d')
        data['update_date'] = instance.update_date.strftime('%Y-%m-%d') if instance.update_date is not None else instance.update_date
        return data
    

class POSTWattmeterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Wattmeter
        fields = ['wattmeter_number', 'wattmeter_brand', 'insert_date', 'update_date']
        read_only_fields = ['insert_date']