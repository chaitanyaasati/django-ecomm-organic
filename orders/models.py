from django.db import models
from users.models import Authentication, Address
from fruits.models import Fruit

class Orders(models.Model):
    user_id = models.ForeignKey(Authentication,on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address,on_delete=models.CASCADE)
    is_payment_done = models.BooleanField(default= False)
    order_time = models.DateTimeField(auto_now=True)
    delivery_time = models.DateTimeField(auto_now=False)


    def _str_(self):
        return self.user_id

class Items(models.Model):
    order_id = models.ForeignKey(Orders,on_delete=models.CASCADE)
    fruit_id = models.ForeignKey(Fruit,on_delete=models.CASCADE)
    quantity = models.FloatField()
    price = models.DecimalField(max_digits=9999999,decimal_places=2)

    def _str_(self):
        return self.order_id