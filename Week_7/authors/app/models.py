from django.db import models

# Create your models here.

class author(models.Model):
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	email_address = models.CharField(max_length = 100)

class publisher(models.Model):
	publisher_name = models.CharField(max_length = 100)
	street = models.CharField(max_length = 100)
	city = models.CharField(max_length = 100)
	state = models.CharField(max_length = 100)	
	country = models.CharField(max_length = 100)
	website = models.CharField(max_length = 100)

class book(models.Model):
	title = models.CharField(max_length = 100)
	publication_date = models.CharField(max_length = 100)
	#authors = models.ManyToManyField(author)
	authors = models.CharField(max_length = 100, default='a')
	publisher = models.ForeignKey(publisher, on_delete=models.CASCADE)