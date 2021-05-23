from rest_framework import serializers  
from .models import Fruit

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = ['id','fruit_name','variety','image'] 

class FruitSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = ['id','fruit_name','variety','image','description']         