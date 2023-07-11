from django.db import models

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


