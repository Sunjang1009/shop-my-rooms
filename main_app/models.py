from django.db import models
from decimal import Decimal

# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    def __str__(self):
        return self.name
    
class Lookbook(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    items = models.TextField(max_length=500, default="Default")
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name="lookbooks")
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('100.00'))
    lookbook = models.ForeignKey(Lookbook, on_delete=models.CASCADE, related_name="products")
    def __str__(self):
        return self.name
    def get_price(self):
        return f"${self.price:,.2f}"

class Shoppinglist(models.Model):
    name = models.CharField(max_length=150)
    products = models.ManyToManyField(Product)
    def __str__(self):
        return self.name
