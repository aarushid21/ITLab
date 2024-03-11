from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class works(models.Model):
    person_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    salary = models.IntegerField()

class lives(models.Model):
    person_name = models.ForeignKey(works, on_delete=models.CASCADE)
    street = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200)    

