from django.urls import include, path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('productlist/', views.product_list, name='product_list'),
    path('product/', views.product, name='product'),
    path('search/',views.search,name='search'),
    path('address/',views.address,name='address'),
    path('addaddress/',views.addAddress,name='addaddress'),
    path('deleteaddress/',views.deleteAddress,name='deleteaddress'),
    path('empty/',views.empty_view),
]