from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=100)
    num_visits = models.IntegerField(default=0)
    num_sites = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

@receiver(post_save, sender=Page)
def update_category_num_sites(sender, instance, created, **kwargs):
    if created:
        instance.category.num_sites += 1
        instance.category.save()