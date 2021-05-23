from fruits.models import Fruit
from .models import Stock 
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StockSerializer,StockSingleSerializer

# Create your views here.
@api_view(['GET'])
def fruitlist(request):
    query = request.query_params['query']
    words=query.split()
    stocks=[]
    for i in words:
        stocks+=Stock.objects.filter(fruit_id__fruit_name__contains=i)
    serializer=StockSerializer(stocks,many=True,context={'request':request})
    return Response(serializer.data)

@api_view(['GET'])
def fruit(request):
    fruitid=request.query_params['fruitid']
    farmid=request.query_params['farmid']
    fruit=Stock.objects.get(fruit_id=fruitid,farm_id=farmid,quantity__gt=0)
    serializer=StockSingleSerializer(fruit,context={'request':request})
    return Response(serializer.data)    