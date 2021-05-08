from django.urls import include, path
from . import views

urlpatterns = [
    path('query/',views.stockquery),
    path('fruitquery/',views.fruitquery)
]