from django.urls import include, path
from . import views

urlpatterns = [
    path('api/order', views.order, name='order'),
]