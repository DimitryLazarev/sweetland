from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=20)
    image = models.FileField(upload_to='static/sweetlandapp')
    description = models.CharField(max_length=35)
    full_description = models.CharField(max_length=255)
    product_type = models.CharField(max_length=50)
    price = models.FloatField()


class Cart(models.Model):
    name = models.CharField(max_length=20)
    image = models.FileField(upload_to='static/sweetlandapp')
    description = models.CharField(max_length=35)
    full_description = models.CharField(max_length=255)
    product_type = models.CharField(max_length=15)
    price = models.FloatField()
    quantity = models.IntegerField()
    product = models.OneToOneField(
        'Products',
        null=True,
        on_delete=models.SET_NULL,
        related_name='product',
    )
