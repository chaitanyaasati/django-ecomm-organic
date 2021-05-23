from django.db import models
from fruits.models import Fruit
from django.contrib.auth.models import User
from farms.models import Farm

class Orders(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    is_payment_done = models.BooleanField(default= False)
    order_time = models.DateTimeField(auto_now=True)
    delivery_time = models.DateTimeField(auto_now=False)


    def _str_(self):
        return self.user_id

class Items(models.Model):
    order_id = models.ForeignKey(Orders,on_delete=models.CASCADE)
    fruit_id = models.ForeignKey(Fruit,on_delete=models.CASCADE)
    farm_id = models.ForeignKey(Farm,on_delete=models.CASCADE)
    quantity = models.FloatField()
    price = models.DecimalField(max_digits=9999999,decimal_places=2)

    def _str_(self):
        return self.order_id