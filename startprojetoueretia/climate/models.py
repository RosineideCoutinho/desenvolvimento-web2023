from django.db import models
#previsão
# Create your models here.
class Forecast (models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    temperature = models.CharField(max_length=14)
    description = models.CharField(max_length=30)
    humidity = models.CharField(max_length=30)
    wind = models.CharField(max_length=30)






