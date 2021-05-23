from django.db import models
from fruits.models import Fruit
from farms.models import Farm

class Stock(models.Model):
    MEDIUM = 'M'
    HIGH = 'H'
    QUALITY_TYPE= [
        (MEDIUM, 'Medium'),
        (HIGH,'High')
    ]
    quality = models.CharField(max_length=1, choices = QUALITY_TYPE,default=MEDIUM)
    price = models.DecimalField(max_digits=999999,decimal_places=2)
    discount = models.FloatField()
    quantity = models.FloatField()
    fruit_id = models.ForeignKey(Fruit,on_delete = models.CASCADE)
    farm_id = models.ForeignKey(Farm, on_delete = models.CASCADE)
    
    def _str_(self):
        return self.farm_id
