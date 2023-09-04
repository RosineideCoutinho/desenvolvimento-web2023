from django.db import models

# Create your models here.
class suggestion (models.Model):
    article = models.CharField(max_length=40)
    # article- artigo.
