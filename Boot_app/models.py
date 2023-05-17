from django.db import models

# Create your models here.


class Register(models.Model):
    roll = models.CharField(max_length=20)
    name = models.CharField(max_length=60)
    mail=models.CharField(max_length=50)
    address = models.TextField()
    backlog = models.IntegerField()


class Details(models.Model):
    roll = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    mail=models.EmailField(max_length=30)
    phone = models.IntegerField()
    dob = models.DateField()
    addar = models.IntegerField()
    pan = models.CharField(max_length=10)
    bacc = models.IntegerField()
    bifsc = models.CharField(max_length=10) 
