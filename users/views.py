from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout
from django.http import HttpResponse
import re
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .functions import validate_email
from django.shortcuts import redirect

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['email'] = self.user.email
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])    
# def usertprofile(request):
#     # user = request.user
#     # serializer = UserSerializer(user, many=False)
#     return Response({"name":"sdfs"})

@api_view(['POST'])
def apiusersignup(request):
    if request.method == "POST":
        message = {}
        context = {}
        message['email'] = []
        message['password'] = []
        message['firstname'] = []
        message['lastname'] = []
        message['confirmpassword'] = []
        context['firstname'] = request.data.get('firstname',None)
        context['lastname'] = request.data.get('lastname',None)
        context['email'] = request.data.get('email',None)
        context['password'] = request.data.get('password',None)
        context['confirmpassword'] = request.data.get('confirmpassword',None)
        user = User.objects.filter(username=request.data.get('email',None))
        if request.data.get('email',None) == "" or request.data.get('email',None)==None:
            message['email'].append('Please enter Email')
            context['message'] = message
            return Response(context)
        elif(len(user) != 0):
            message['email'].append('Account already exists with this email')
            context['message'] = message
            return Response(context)
        elif request.data.get('firstname',None) == "" or request.data.get('firstname',None) == None:
            message['firstname'].append('Please enter First Name')
            context['message'] = message
            print(context)
            return Response(context)
        elif request.data['lastname'] == "" or request.data.get('lastname',None) == None:
            message['lastname'].append('Please enter last name')
            context['message'] = message
            return Response(context)
        elif request.data['password'] == "" or request.data.get('password',None) == None:
            message['password'].append('Please enter Password')
            context['message'] = message
            return Response(context)
        elif request.data.get('confirmpassword',None) == "" or request.data.get('confirmpassword',None) == None:
            message['confirmpassword'].append('Please enter Password again')
            context['message'] = message
            return Response(context)
        else:
            if validate_email(request.data.get('email')):
                if(request.data.get('password') == request.data.get('confirmpassword')):
                    user = User.objects.create_user(
                        request.data['email'], request.data['email'], request.data['password'])
                    user.last_name = request.data['lastname']
                    user.first_name = request.data['firstname']
                    user.save()
                    return Response({"message":"Your account is created"})
                else:
                    message['confirmpassword'] = [
                        'Password and Confirm Password not matching']
                    print(message)
                    context = {"message": message}
                    return Response(context)
            else:
                message['email'].append('Email is not in valid format')
                context['message'] = message
                context['confirmpassword'] = request.data['confirmpassword']
                return Response(context)

@api_view(['GET'])
def apiuserprofile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


#http signup view 
def usersignup(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'users/signup.html')
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

            return render(request, 'users/signup.html', context)
        elif(len(user) != 0):
            message['email'].append('Account already exists with this email')
            context['message'] = message
            return render(request, 'users/signup.html', context)
        elif request.POST['firstname'] == "":
            message['firstname'].append('Please enter First Name')
            context['message'] = message
            print(context)
            return render(request, 'users/signup.html', context)
        elif request.POST['lastname'] == "":
            message['lastname'].append('Please enter last name')
            context['message'] = message
            return render(request, 'users/signup.html', context)
        elif request.POST['password'] == "":
            message['password'].append('Please enter Password')
            context['message'] = message
            return render(request, 'users/signup.html', context)
        elif request.POST['confirmpassword'] == "":
            message['confirmpassword'].append('Please enter Password again')
            context['message'] = message
            return render(request, 'users/signup.html', context)

        else:
            if validate_email(request.POST['email']):
                if(request.POST['password'] == request.POST['confirmpassword']):
                    user = User.objects.create_user(
                        request.POST['email'], request.POST['email'], request.POST['password'])
                    user.last_name = request.POST['lastname']
                    user.first_name = request.POST['firstname']
                    user.save()
                    # account is created
                    return redirect('home')
                else:
                    message['confirmpassword'] = [
                        'Password and Confirm Password not matching']
                    print(message)
                    context = {"message": message}
                    return render(request, 'users/signup.html', context)
            else:
                message['email'].append('Email is not in valid format')
                context['message'] = message
                context['confirmpassword'] = request.POST['confirmpassword']
                return render(request, 'users/signup.html', context)                      

# http login view
def userlogin(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('home')
        print(request.user)
        return render(request, 'users/login.html')
    else:
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            message = "username and password combination does not match"
            context = {}
            context['message'] = message
            print(context)
            return render(request, 'users/login.html', context)

#http logout view
def userlogout(request):
    if request.method == "GET":
        logout(request)
        return redirect('home')            


def home(request):
    return render(request,'users/home.html')

def singleproduct(request):
    return render(request,'users/product.html')    