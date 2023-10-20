from django.db import models


# Create your models here.
class Country(models.Model):
    country_name=models.CharField(max_length=20)

