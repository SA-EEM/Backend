from django.utils import timezone
from rest_framework import serializers
#Modelos necesarios: (ordenados)
##Status, Servicios, Marca de Contador, Rutas, Aldeas/Pueblo, Poste eléctrico, Tipo de Identificación, Roles, Departamentos
from tasks.models.models import (Status, 
                                Services, 
                                WattmeterBrand, 
                                Route, 
                                Village, 
                                ElectricPole,
                                IdentificationType,
                                Roles,
                                Departments
                            )

#TODO: Serializadores básicos para cada modelo catálogo, utilizando ModelSerializer

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'status_name', 'insert_date', 'update_date']
        read_only_fields = ['insert_date']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['insert_date'] = instance.insert_date.strftime('%Y-%m-%d')
        representation['update_date'] = instance.update_date.strftime('%Y-%m-%d') if instance.update_date is not None else instance.update_date
        return representation
    
    def update(self, instance, validated_data):
        instance.update_date = timezone.now()
        instance.status_name = validated_data.get('status_name')
        instance.save(update_fields=['status_name', 'update_date'])
        return instance

class ServiceSerializer(serializers.ModelSerializer):
    pass

class WattmeterBrandSerializer(serializers.ModelSerializer):
    pass

class RouteSerializer(serializers.ModelSerializer):
    pass

class VillageSerializer(serializers.ModelSerializer):
    pass

class ElectricPoleSerializer(serializers.ModelSerializer):
    pass

class IdentificationTypeSerializer(serializers.ModelSerializer):
    pass

class RolesSerializer(serializers.ModelSerializer):
    pass

class DepartmentsSerializer(serializers.ModelSerializer):
    pass