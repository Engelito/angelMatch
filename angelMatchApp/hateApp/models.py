from django.db import models

# Create your models here.
class hateApp(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    hatefood = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    