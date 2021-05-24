from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .functions import validate_email
from django.contrib.auth import authenticate, login, logout
from stock.models import Stock


def signin(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('product_list')
        print(request.user)
        return render(request, 'webappdemo/pages/signin.html')
    elif request.method=="POST":
        print("iampost")
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        print(request.POST['username'])    
        print(request.POST['password'])    
        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            message = "username and password combination does not match"
            print(message)
            context = {}
            context['message'] = message
            print(context)
            return render(request, 'webappdemo/pages/signin.html', context)



def signup(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('product_list')
        return render(request, 'webappdemo/pages/signup.html')
    elif request.method == "POST":
        message = {}
        context = {}
        message['email'] = []
        message['password'] = []
        message['firstname'] = []
        message['lastname'] = []
        message['confirmpassword'] = []
        context['firstname'] = request.POST['firstname']
        context['lastname'] = request.POST['lastname']
        context['email'] = request.POST['email']
        context['password'] = request.POST['password']
        context['confirmpassword'] = request.POST['confirmpassword']
        print(request.POST.get('firstname', None))
        user = User.objects.filter(username=request.POST['email'])
        print("")
        if request.POST['email'] == "":
            message['email'].append('Please enter Email')
            context['message'] = message

            return render(request, 'webappdemo/pages/signup.html', context)
        elif(len(user) != 0):
            message['email'].append('Account already exists with this email')
            context['message'] = message
            return render(request, 'webappdemo/pages/signup.html', context)
        elif request.POST['firstname'] == "":
            message['firstname'].append('Please enter First Name')
            context['message'] = message
            print(context)
            return render(request, 'webappdemo/pages/signup.html', context)
        elif request.POST['lastname'] == "":
            message['lastname'].append('Please enter last name')
            context['message'] = message
            return render(request, 'webappdemo/pages/signup.html', context)
        elif request.POST['password'] == "":
            message['password'].append('Please enter Password')
            context['message'] = message
            return render(request, 'webappdemo/pages/signup.html', context)
        elif request.POST['confirmpassword'] == "":
            message['confirmpassword'].append('Please enter Password again')
            context['message'] = message
            return render(request, 'webappdemo/pages/signup.html', context)

        else:
            if validate_email(request.POST['email']):
                if(request.POST['password'] == request.POST['confirmpassword']):
                    user = User.objects.create_user(
                        request.POST['email'], request.POST['email'], request.POST['password'])
                    user.last_name = request.POST['lastname']
                    user.first_name = request.POST['firstname']
                    user.save()
                    # account is created
                    message['success']=['Account is successfully created. Please login']
                    context = {"message":message}
                    return render(request, 'webappdemo/pages/signup.html', context)
                else:
                    message['confirmpassword'] = [
                        'Password and Confirm Password not matching']
                    print(message)
                    context = {"message": message}
                    return render(request, 'webappdemo/pages/signup.html', context)
            else:
                message['email'].append('Email is not in valid format')
                context['message'] = message
                context['confirmpassword'] = request.POST['confirmpassword']
                return render(request, 'webappdemo/pages/signup.html', context)

def product_list(request):
    return render(request,'webappdemo/pages/product-list.html')

def product(request):
    return render(request,'webappdemo/pages/product.html')

def cart(request):
    return render(request,'webappdemo/pages/cart.html')

def signout(request):
    if request.method == "GET":
        logout(request)
        return redirect('product_list')   

def search(request):
    if request.method == 'GET':
        query=request.GET['search']
        words=query.split()
        stocks=[]
        context={}
        for i in words:
            stocks+=Stock.objects.filter(fruit_id__fruit_name__contains=i)
        context['stocks']=stocks
        return render(request,'webappdemo/pages/search.html',context)