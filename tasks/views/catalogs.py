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
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer

class WattmeterBrandViewSet(viewsets.ModelViewSet):
    queryset = WattmeterBrand.objects.all()
    serializer_class = WattmeterBrandSerializer

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class VillageViewSet(viewsets.ModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
  
class ElectricPoleViewSet(viewsets.ModelViewSet):
    queryset = ElectricPole.objects.all()
    serializer_class = ElectricPoleSerializer

class IdentificationTypeViewSet(viewsets.ModelViewSet):
    queryset = IdentificationType.objects.all()
    serializer_class = IdentificationTypeSerializer
 
class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
 
class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer
