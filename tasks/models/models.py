# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountData(models.Model):
    wattmeter = models.ForeignKey('Wattmeter', models.DO_NOTHING)
    request_date = models.DateTimeField()
    opening_date = models.DateTimeField(blank=True, null=True)
    id_home_information = models.ForeignKey('HomeInformation', models.DO_NOTHING, db_column='id_home_information')
    reading_order = models.IntegerField(blank=True, null=True)
    custom_mark = models.IntegerField(blank=True, null=True)
    id_services = models.ForeignKey('Services', models.DO_NOTHING, db_column='id_services')
    id_client = models.ForeignKey('Client', models.DO_NOTHING, db_column='id_client')
    volts_requested = models.IntegerField(blank=True, null=True)
    cumulative_reading = models.IntegerField(blank=True, null=True)
    id_status = models.ForeignKey('Status', models.DO_NOTHING, db_column='id_status')
    id_read_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_read_user')
    next_visit_date = models.DateField(blank=True, null=True)
    watts_hired = models.FloatField(blank=True, null=True)
    id_electric_pole = models.OneToOneField('ElectricPole', models.DO_NOTHING, db_column='id_electric_pole')
    exent_iva = models.IntegerField(blank=True, null=True)
    exent_percentaje = models.FloatField(blank=True, null=True)
    electric_transformer = models.CharField(max_length=30, blank=True, null=True)
    phase = models.PositiveIntegerField(blank=True, null=True)
    id_route = models.ForeignKey('Route', models.DO_NOTHING, db_column='id_route')
    visit_date = models.DateField(blank=True, null=True)
    ap_amount = models.FloatField(blank=True, null=True)
    installation_invoice = models.CharField(max_length=25, blank=True, null=True)
    pay_date = models.DateField(blank=True, null=True)
    contract_number = models.CharField(max_length=15, blank=True, null=True)
    pay_docs = models.CharField(max_length=75, blank=True, null=True)
    central_number = models.CharField(max_length=15, blank=True, null=True)
    net_type = models.IntegerField(blank=True, null=True)
    pole_meters = models.PositiveIntegerField(blank=True, null=True)
    pay_amount = models.FloatField(blank=True, null=True)
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user', related_name='accountdata_id_user_set')
    insert_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_data'


class Client(models.Model):
    first_name = models.CharField(max_length=35)
    middle_name = models.CharField(max_length=35, blank=True, null=True)
    third_name = models.CharField(max_length=35, blank=True, null=True)
    first_lastname = models.CharField(max_length=35)
    second_lastname = models.CharField(max_length=35)
    married_name = models.CharField(max_length=35, blank=True, null=True)
    nit = models.PositiveIntegerField(unique=True)
    email = models.CharField(unique=True, max_length=50, blank=True, null=True)
    phone_number = models.PositiveIntegerField()
    identification = models.ForeignKey('IdentificationType', models.DO_NOTHING)
    insert_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'


class Departments(models.Model):
    department_name = models.CharField(max_length=25, blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class ElectricPole(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    insert_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'electric_pole'


class HomeInformation(models.Model):
    municipality_name = models.CharField(max_length=25, blank=True, null=True)
    addres = models.CharField(max_length=50)
    zone_number = models.PositiveIntegerField()
    reference = models.CharField(max_length=50, blank=True, null=True)
    id_village = models.ForeignKey('Village', models.DO_NOTHING, db_column='id_village')
    insert_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_information'


class IdentificationType(models.Model):
    identification_name = models.CharField(max_length=25)
    insert_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'identification_type'


class Login(models.Model):
    username = models.CharField(unique=True, max_length=25)
    password = models.CharField(max_length=25)
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')
    insert_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login'


class Roles(models.Model):
    rol_name = models.CharField(max_length=25, blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Route(models.Model):
    route_name = models.CharField(unique=True, max_length=50)
    insert_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'route'


class Services(models.Model):
    service_name = models.CharField(unique=True, max_length=50)
    insert_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services'


class Status(models.Model):
    status_name = models.CharField(unique=True, max_length=25)
    insert_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status'


class Users(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    insert_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    rol = models.ForeignKey(Roles, models.DO_NOTHING)
    department = models.ForeignKey(Departments, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users'


class Village(models.Model):
    village_name = models.CharField(unique=True, max_length=50)
    insert_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'village'


class Wattmeter(models.Model):
    wattmeter_number = models.IntegerField(unique=True)
    wattmeter_brand = models.ForeignKey('WattmeterBrand', models.DO_NOTHING)
    insert_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wattmeter'


class WattmeterBrand(models.Model):
    brand_name = models.CharField(max_length=50)
    insert_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wattmeter_brand'
