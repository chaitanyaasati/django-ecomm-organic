from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
def order(request):
    return Response({"ordered":"True"})