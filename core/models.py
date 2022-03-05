from operator import mod
from statistics import mode
from django.db import models
from validators import Max

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=60)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    