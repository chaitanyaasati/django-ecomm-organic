from fruits.models import Fruit
from farms.models import Farm
from .models import Stock
from rest_framework import serializers 
from farms.serializers import FarmSerializer
from fruits.serializers import FruitSerializer,FruitSingleSerializer                    

class StockSerializer(serializers.ModelSerializer):
    fruit = FruitSerializer(source='fruit_id')
    farm = FarmSerializer(source='farm_id')
    class Meta:
        model = Stock
        fields = ['price', 'discount', 'quality', 'fruit', 'farm']  

class StockSingleSerializer(serializers.ModelSerializer):
    fruit = FruitSingleSerializer(source='fruit_id')
    farm = FarmSerializer(source='farm_id')
    class Meta:
        model = Stock
        fields = ['price', 'discount', 'quality', 'fruit', 'farm']                 