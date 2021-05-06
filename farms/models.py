from django.db import models
from users.models import Authentication, Address

class Farm(models.Model):
    farm_name = models.CharField(max_length=100)
    user_id = models.ForeignKey(Authentication,on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address,on_delete=models.CASCADE)
   

    def _str_(self):
        return self.user_id