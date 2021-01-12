from rest_framework import serializers

from contacts.models import SaleContact, RentContact

class SaleContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleContact
        fields = '__all__'

class  RentContactSerializer(serializers.ModelSerializer):
    class Meta:
        model =  RentContact
        fields = '__all__'