from django.db import models

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=300, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="product_imgs")

    def __str__(self):
        return self.name