from django.urls import include, path
from . import views

urlpatterns = [
    path('api/account/signup', views.apiusersignup, name='apiusersignup'),
    path('api/account/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/account/profile', views.apiuserprofile, name='apiuserprofile'),
    path('account/signup', views.usersignup, name='usersignup'),
    path('account/login', views.userlogin, name='userlogin'),
    path('account/logout', views.userlogout, name='userlogout'),
    path('account/home', views.home, name='home'),
    path('account/product', views.singleproduct, name='singleproduct')
]