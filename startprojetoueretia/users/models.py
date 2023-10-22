from django.db import models

# Create your models here.
class Login (models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

 def __str__(self):
        return  self.nome
