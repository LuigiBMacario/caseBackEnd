from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    address = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    civil_status = models.CharField(max_length=100)
    def __str__(self):
        return self.name
