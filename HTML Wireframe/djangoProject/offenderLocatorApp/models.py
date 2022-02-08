from pickle import TRUE
from tabnanny import verbose
from django.db import models
from datetime import datetime


from django.forms import CharField, DateField, IntegerField


# Create your models here.


class offenders1(models.Model):
    status = (
        ("Ongoing","Ongoing"),
        ("Released","Released"),
        ("Transferred","Transferred"),
    )
    offender = models.CharField(max_length=45, verbose_name='offender')
    gender = models.CharField(max_length=6, verbose_name='gender')
    age = models.IntegerField()
    offense = models.CharField(max_length=45, verbose_name='offense')
    caseStatus = models.CharField(max_length=11, choices=status, default='Ongoing')
    caseDescription = models.TextField(max_length = 400,null = TRUE,verbose_name='caseDescription')
    

    
class offenders2(models.Model):
    newpassword = models.CharField(max_length=12, verbose_name='newpassword')
    password = models.CharField(max_length=12, verbose_name='password',default = 'admin')
    
