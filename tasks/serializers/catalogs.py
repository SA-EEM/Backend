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
    class Meta:
        model = Services
        fields = ['id', 'service_name', 'insert_date', 'update_date']
        read_only_fields = ['insert_date']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['insert_date'] = instance.insert_date.strftime('%Y-%m-%d')
        representation['update_date'] = instance.update_date.strftime('%Y-%m-%d') if instance.update_date is not None else instance.update_date
        return representation
    
    def update(self, instance, validated_data):
        instance.update_date = timezone.now()
        instance.service_name = validated_data.get('service_name')
        instance.save(update_fields=['service_name', 'update_date'])
        return instance

class WattmeterBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = WattmeterBrand
        fields = ['id', 'brand_name', 'insert_date', 'update_date']
        read_only_fields = ['insert_date']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['insert_date'] = instance.insert_date.strftime('%Y-%m-%d')
        representation['update_date'] = instance.update_date.strftime('%Y-%m-%d') if instance.update_date is not None else instance.update_date
        return representation
    
    def update(self, instance, validated_data):
        instance.update_date = timezone.now()
        instance.brand_name = validated_data.get('brand_name')
        instance.save(update_fields=['brand_name', 'update_date'])
        return instance
    

class RouteSerializer(serializers.ModelSerializer):
    class Meta:    
        model = Route
        fields = ['id', 'route_name', 'insert_date', 'update_date']
        read_only_fields = ['insert_date']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['insert_date'] = instance.insert_date.strftime('%Y-%m-%d')
        representation['update_date'] = instance.update_date.strftime('%Y-%m-%d') if instance.update_date is not None else instance.update_date
        return representation
    
    def update(self, instance, validated_data):
        instance.update_date = timezone.now()
        instance.route_name = validated_data.get('route_name')
        instance.save(update_fields=['route_name', 'update_date'])
        return instance

    

class VillageSerializer(serializers.ModelSerializer):
    class Meta:    
        model = Village
        fields = ['id', 'village_name', 'insert_date', 'update_date']
        read_only_fields = ['insert_date']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['insert_date'] = instance.insert_date.strftime('%Y-%m-%d')
        representation['update_date'] = instance.update_date.strftime('%Y-%m-%d') if instance.update_date is not None else instance.update_date
        return representation
    
    def update(self, instance, validated_data):
        instance.update_date = timezone.now()
        instance.village_name = validated_data.get('village_name')
        instance.save(update_fields=['village_name', 'update_date'])
        return instance

class ElectricPoleSerializer(serializers.ModelSerializer):
    class Meta:    
        model = ElectricPole
        fields = ['id', 'insert_date', 'update_date']
        read_only_fields = ['insert_date']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['insert_date'] = instance.insert_date.strftime('%Y-%m-%d')
        representation['update_date'] = instance.update_date.strftime('%Y-%m-%d') if instance.update_date is not None else instance.update_date
        return representation
    
    def update(self, instance, validated_data):
        instance.update_date = timezone.now()
        instance.save()
        return instance

class IdentificationTypeSerializer(serializers.ModelSerializer):
    class Meta:    
        model = IdentificationType
        fields = ['id', 'identification_name', 'insert_date', 'update_date']
        read_only_fields = ['insert_date']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['insert_date'] = instance.insert_date.strftime('%Y-%m-%d')
        representation['update_date'] = instance.update_date.strftime('%Y-%m-%d') if instance.update_date is not None else instance.update_date
        return representation
    
    def update(self, instance, validated_data):
        instance.update_date = timezone.now()
        instance.identification_name = validated_data.get('identification_name')
        instance.save(update_fields=['identification_name', 'update_date'])
        return instance


class RolesSerializer(serializers.ModelSerializer):
    class Meta:    
        model = Roles
        fields = ['id', 'rol_name', 'insert_date', 'update_date']
        read_only_fields = ['insert_date']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['insert_date'] = instance.insert_date.strftime('%Y-%m-%d')
        representation['update_date'] = instance.update_date.strftime('%Y-%m-%d') if instance.update_date is not None else instance.update_date
        return representation
    
    def update(self, instance, validated_data):
        instance.update_date = timezone.now()
        instance.rol_name = validated_data.get('rol_name')
        instance.save(update_fields=['rol_name', 'update_date'])
        return instance


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:    
        model = Departments
        fields = ['id', 'department_name', 'insert_date', 'update_date']
        read_only_fields = ['insert_date']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['insert_date'] = instance.insert_date.strftime('%Y-%m-%d')
        representation['update_date'] = instance.update_date.strftime('%Y-%m-%d') if instance.update_date is not None else instance.update_date
        return representation
    
    def update(self, instance, validated_data):
        instance.update_date = timezone.now()
        instance.department_name = validated_data.get('department_name')
        instance.save(update_fields=['department_name', 'update_date'])
        return instance
