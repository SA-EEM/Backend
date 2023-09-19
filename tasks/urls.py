from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
#Vistas Catálogos Viewsets
from tasks.views.catalogs import (
    StatusViewSet,
    ServiceViewSet,
    WattmeterBrandViewSet,
    RouteViewSet,
    VillageViewSet,
    ElectricPoleViewSet,
    IdentificationTypeViewSet,
    RolesViewSet,
    DepartmentsViewSet
    )
from tasks.views.home_info import HomeInfoViewSet

router = routers.DefaultRouter()

router.register('catalog/status', StatusViewSet, basename='status')
router.register('catalog/service', ServiceViewSet, basename='service')
router.register('catalog/wattmeterBrand', WattmeterBrandViewSet, basename='wattmeterBrand')
router.register('catalog/route', RouteViewSet, basename='route')
router.register('catalog/village', VillageViewSet, basename='village')
router.register('catalog/electricPole', ElectricPoleViewSet, basename='electricPole')
router.register('catalog/identificationType', IdentificationTypeViewSet, basename='identificationType')
router.register('catalog/roles', RolesViewSet, basename='roles')
router.register('catalog/departments', DepartmentsViewSet, basename='departments')
router.register('homeInformation', HomeInfoViewSet, basename='homeInformation')

# router.register(r'tasks', views.TaskView, 'tasks')

urlpatterns = [
    #URLs desde registro de router(catálogos):
    path('', include(router.urls))
    
    #Paths as_view()
    # path("api/v1/", include(router.urls)),
    # path("docs/", include_docs_urls(title="Task API"))
]