from rest_framework import serializers
#Modelo
from tasks.models.models import Users
#Serializadores
from .catalogs import DepartmentsSerializer, RolesSerializer

class GETUsersSerializer(serializers.ModelSerializer):
    rol = RolesSerializer(many=False, read_only=True)
    department = DepartmentsSerializer(many=False, read_only=True)
    
    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'status', 'rol', 'department','insert_date', 'update_date']
        read_only_fields = ['insert_date']
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['rol'] = RolesSerializer(instance.rol).data
        data['department'] = DepartmentsSerializer(instance.department).data
        data['insert_date'] = instance.insert_date.strftime('%Y-%m-%d')
        data['update_date'] = instance.update_date.strftime('%Y-%m-%d') if instance.update_date is not None else instance.update_date
        return data
    

class POSTUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'status', 'rol', 'department','insert_date', 'update_date']
        read_only_fields = ['insert_date']