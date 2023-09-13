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
    pass

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