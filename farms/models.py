from django.db import models
from users.models import Address, Pincode
from django.contrib.auth.models import User

class Seller(models.Model):
    seller_name = models.CharField(max_length=100)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def _str_(self):
        return self.seller_name

class Farm(models.Model):
    farm_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    seller_id = models.ForeignKey(Seller,on_delete=models.CASCADE)
    pincode_id = models.ForeignKey(Pincode,on_delete=models.CASCADE)
   
    def _str_(self):
        return self.farm_name        