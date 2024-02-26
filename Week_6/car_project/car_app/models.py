from django.db import models

# Create your models here.

class Car(models.Model):
    manufacturer = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)