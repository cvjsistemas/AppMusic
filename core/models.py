from django.db import models

# Create your models here.
class Product (models.Model):
    product_id=models.AutoField(primary_key=True)
    product_nombre=models.CharField(max_length=80,unique=True)
    product_description=models.TextField(blank=True,null=True)
    product_price=models.DecimalField(max_digits=7,decimal_places=2)


    def __str__(self):
        return self.product_nombre