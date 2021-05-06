from django.db import models

class Fruit(models.Model):
    fruit_name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, null=True)
    variety = models.CharField(max_length=120)
    image = models.ImageField(upload_to="fruits/fruit",blank=True)

    def _str_(self):
        return self.fruit_name