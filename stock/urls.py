from django.urls import include, path
from . import views

urlpatterns = [
    path('query/',views.fruitlist),
    path('fruit/',views.fruit)
]