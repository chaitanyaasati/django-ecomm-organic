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
        fields = ['id','price', 'discount', 'quality', 'fruit', 'farm']  

class StockSingleSerializer(serializers.ModelSerializer):
    fruit = FruitSingleSerializer(source='fruit_id')
    farm = FarmSerializer(source='farm_id')
    class Meta:
        model = Stock
        fields = ['id','price', 'discount', 'quality', 'fruit', 'farm']   

class StockDoubleSerializer(serializers.ModelSerializer):
    fruitname = serializers.ReadOnlyField(source='fruit_id.fruit_name')
    fruitid = serializers.ReadOnlyField(source='fruit_id.id')
    fruitvariety = serializers.ReadOnlyField(source='fruit_id.variety')
    fruitimage = serializers.ImageField(source='fruit_id.image')
    farm = FarmSerializer(source='farm_id')
    disi=serializers.ReadOnlyField(source='discount')
    class Meta:
        model = Stock
        fields = ['id','price', 'disi','fruitimage', 'quality', 'fruitname', 'fruitid', 'fruitvariety','farm']                       