from django.utils import timezone
from rest_framework import serializers
#Modelo
from tasks.models.models import Users
#Serializadores
from .catalogs import DepartmentsSerializer, RolesSerializer

from rest_framework.authtoken.models import Token

class GETUsersSerializer(serializers.ModelSerializer):
    rol = RolesSerializer(many=False, read_only=True)
    department = DepartmentsSerializer(many=False, read_only=True)
    
    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'username', 'status', 'rol', 'department','insert_date', 'update_date']
        read_only_fields = ['insert_date']
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    
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
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'status', 'rol', 'department','insert_date', 'update_date']
        read_only_fields = ['insert_date']

        extra_kwargs = {
            'password' : {'write_only': True}
        }

    def create(self, validated_data):
        user = Users(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username'],
            status = validated_data['status'],
            rol = validated_data['rol'],
            department = validated_data['department'],
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user = user)
        return user
    
    def update(self, instance, validated_data):
        update_fields = []
        for field in ['first_name', 'last_name', 'username', 'status', 'rol', 'department', 'update_date']:
            if field in validated_data:
                setattr(instance, field, validated_data[field])
                update_fields.append(field)
        
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            update_fields.append('password')
        
        if update_fields:
            instance.update_date = timezone.now()
            instance.save(update_fields=update_fields)
        
        return instance