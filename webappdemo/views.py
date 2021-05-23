from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def signin(request):
    return render(request,'webappdemo/pages/signin.html')

def signup(request):
    return render(request,'webappdemo/pages/signup.html')

def product_list(request):
    return render(request,'webappdemo/pages/product-list.html')

def product(request):
    return render(request,'webappdemo/pages/product.html')

def cart(request):
    return render(request,'webappdemo/pages/cart.html')