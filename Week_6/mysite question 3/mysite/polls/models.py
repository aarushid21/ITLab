from django.db import models

# Create your models here.
class student(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    contact_number = models.CharField(max_length=3, blank = True)

