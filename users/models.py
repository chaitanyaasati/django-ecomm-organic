from django.db import models
from django.contrib.auth.models import User

class Pincode(models.Model):
    pincode = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    
    def _str_(self):
        return self.pincode

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('home')    

class Address(models.Model):
    phone = models.CharField(max_length=50)
    address = models.TextField(max_length=500, null=True)
    pincode = models.ForeignKey(Pincode,null=True,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def _str_(self):
        return self.phone
