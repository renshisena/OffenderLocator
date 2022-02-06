from pickle import TRUE
from tabnanny import verbose
from django.db import models
from datetime import datetime


from django.forms import CharField, DateField, IntegerField


# Create your models here.


class offenders1(models.Model):
    status = (
        ("Ongoing","Ongoing"),
        ("Release","Release"),
        ("Transfer","Transfer"),
    )
    offender = models.CharField(max_length=45, verbose_name='offender')
    gender = models.CharField(max_length=6, verbose_name='gender')
    age = models.IntegerField()
    offense = models.CharField(max_length=45, verbose_name='offense')
    caseStatus = models.CharField(max_length=8, choices=status, default='Ongoing')
    caseDescription = models.TextField(max_length = 400,null = TRUE,verbose_name='caseDescription')
    password = models.CharField(max_length=12, verbose_name='password')
    dateRelease = models.CharField(max_length=3)
    dateTransfer = models.CharField(max_length=3)
    dateComplaint = models.CharField(max_length=3)
    
