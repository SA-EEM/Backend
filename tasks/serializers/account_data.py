from rest_framework import serializers
#Modelo
from tasks.models.models import AccountData, Wattmeter, HomeInformation, Client
#Serializador Village
from .wattmeter import GETWattmeterSerializer, POSTWattmeterSerializer
from .home_info import GETHomeInformationSerializer, POSTHomeInformationSerializer
from .catalogs import ServiceSerializer, StatusSerializer
from .client import GETClientSerializer, POSTClientSerializer
from .users import GETUsersSerializer

class GETAccountDataSerializer(serializers.ModelSerializer):
    id_wattmeter = GETWattmeterSerializer(many=False, read_only=True)
    id_home_information = GETHomeInformationSerializer(many=False, read_only=True)
    id_services = ServiceSerializer(many=False, read_only=True)
    id_client = GETClientSerializer(many=False, read_only=True)
    id_status = StatusSerializer(many=False, read_only=True)
    id_read_user = GETUsersSerializer(many=False, read_only=True)
    id_user = GETUsersSerializer(many=False, read_only=True)
    
    class Meta:
        model = AccountData
        fields = ['id',
            'id_wattmeter',
            'request_date',
            'opening_date',
            'id_home_information',
            'reading_order',
            'custom_mark',
            'id_services',
            'id_client',
            'volts_requested',
            'cumulative_reading',
            'id_status',
            'id_read_user',
            'watts_hired',
            'exent_iva',
            'electric_transformer',
            'phase',
            'visit_date',
            'ap_amount',
            'installation_invoice',
            'contract_number',
            'pay_docs',
            'central_number',
            'net_type',
            'pole_meters',
            'pay_amount',
            'id_user',
            'insert_date', 
            'update_date']
        read_only_fields = ['insert_date']
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['id_wattmeter'] = GETWattmeterSerializer(instance.id_wattmeter).data
        data['id_home_information'] = GETHomeInformationSerializer(instance.id_home_information).data
        data['id_services'] = ServiceSerializer(instance.id_services).data
        data['id_client'] = GETClientSerializer(instance.id_client).data
        data['id_status'] = StatusSerializer(instance.id_status).data
        data['id_read_user'] = GETUsersSerializer(instance.id_read_user).data
        data['id_user'] = GETUsersSerializer(instance.id_user).data
        data['insert_date'] = instance.insert_date.strftime('%Y-%m-%d')
        data['update_date'] = instance.update_date.strftime('%Y-%m-%d') if instance.update_date is not None else instance.update_date
        data['opening_date'] = instance.opening_date.strftime('%Y-%m-%d') if instance.opening_date is not None else instance.opening_date
        return data
    

class POSTAccountDataSerializer(serializers.ModelSerializer):
    id_home_information = POSTHomeInformationSerializer(many=False)
    
    class Meta:
        model = AccountData
        fields = ['id',
            'id_wattmeter',
            'request_date',
            'opening_date',
            'id_home_information',
            'reading_order',
            'custom_mark',
            'id_services',
            'id_client',
            'volts_requested',
            'cumulative_reading',
            'id_status',
            'id_read_user',
            'watts_hired',
            'exent_iva',
            'electric_transformer',
            'phase',
            'visit_date',
            'ap_amount',
            'installation_invoice',
            'contract_number',
            'pay_docs',
            'central_number',
            'net_type',
            'pole_meters',
            'pay_amount',
            'id_user',
            'insert_date', 
            'update_date']
        read_only_fields = ['insert_date']
    
    def create(self, validated_data):
        home_info_data = validated_data.pop('id_home_information')
        
        # Crea los objetos relacionados y asigna sus valores
        home_info_instance = HomeInformation.objects.create(**home_info_data)
        
        # Asigna los objetos relacionados a la instancia de AccountData
        validated_data['id_home_information'] = home_info_instance
        
        account = AccountData.objects.create(**validated_data)
        
        return account
    

