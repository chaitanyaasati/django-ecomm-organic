from django.shortcuts import render
from fruits.models import Fruit
from .models import Stock 
from rest_framework import serializers
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'  
        depth = 2     

# Create your views here.
@api_view(['GET'])
def stockquery(request):
    query = request.query_params['query']
    print(query)
    words=query.split()
    fruits=[]
    # d=Stock.objects.all()
    for i in words:
        fruits+=Fruit.objects.filter(fruit_name__contains=i)
    # f=s[0].stock_set.all()
    f=Stock.objects.filter(fruit_id__in=fruits)
    serializer=StockSerializer(f,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def fruitquery(request):
    fruitid=request.query_params['id']
    # f=s[0].stock_set.all()
    # f=Stock.objects.filter(fruit_id=fruitid)
    f=Stock.objects.filter(fruit_id__description='sdvcs',farm_id__farm_name="ganesh")
    serializer=StockSerializer(f,many=True)
    return Response(serializer.data)    