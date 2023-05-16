from django.db import models

# Create your models here.


class Register(models.Model):
    roll = models.CharField(max_length=20)
    name = models.CharField(max_length=60)
    mail=models.CharField(max_length=50)
    address = models.TextField()
    backlog = models.IntegerField()