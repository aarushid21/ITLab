from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=3)
    subject = models.CharField(max_length=100)