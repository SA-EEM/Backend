from rest_framework import viewsets
#Modelos
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
#Serializadores
from tasks.serializers.catalogs import (StatusSerializer,
                                        ServiceSerializer,
                                        WattmeterBrandSerializer,
                                        RouteSerializer,
                                        VillageSerializer,
                                        ElectricPoleSerializer,
                                        IdentificationTypeSerializer,
                                        RolesSerializer,
                                        DepartmentsSerializer
                                        )

#TODO: desarrollo de las vistas para los serializadores creados, utilizando ModelViewSet

class StatusViewSet(viewsets.ModelViewSet):
    pass

class ServiceViewSet(viewsets.ModelViewSet):
    pass

class WattmeterBrandViewSet(viewsets.ModelViewSet):
    pass

class RouteViewSet(viewsets.ModelViewSet):
    pass

class VillageViewSet(viewsets.ModelViewSet):
    pass

class ElectricPoleViewSet(viewsets.ModelViewSet):
    pass

class IdentificationTypeViewSet(viewsets.ModelViewSet):
    pass

class RolesViewSet(viewsets.ModelViewSet):
    pass

class DepartmentsViewSet(viewsets.ModelViewSet):
    pass