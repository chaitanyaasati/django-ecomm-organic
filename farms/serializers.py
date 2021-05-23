from rest_framework import serializers
from .models import Farm,Seller

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['seller_name']

class FarmSerializer(serializers.ModelSerializer):
    seller = SellerSerializer(source='seller_id')
    class Meta:
        model = Farm
        fields = ['id','farm_name','seller']


