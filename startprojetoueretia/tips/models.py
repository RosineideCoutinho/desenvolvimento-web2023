from django.db import models

# Create your models here.
class Suggestion (models.Model):
    article = models.CharField(max_length=40)
    # article- artigo.
 def __str__(self):
        return  self.article
