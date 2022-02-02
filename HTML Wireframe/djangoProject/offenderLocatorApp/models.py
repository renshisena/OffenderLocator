from tabnanny import verbose
from django.db import models
from datetime import datetime

from django.forms import CharField, DateField, IntegerField


# Create your models here.
class offenders(models.Model):
    offender = models.CharField(max_length=45, verbose_name='offender')
    gender = models.CharField(max_length=6, verbose_name='gender')
    age = models.PositiveSmallIntegerField(verbose_name='age')
    offenderID = CharField(verbose_name= 'offenderID')
    offense = models.CharField(max_length=4, verbose_name='offense')
    caseStatus= models.CharField(max_length=8, verbose_name='caseStatus')
    caseDescription = models.TextField(verbose_name='caseDescription')
    password = models.CharField(max_length=12, verbose_name='password')
    dateRelease = models.DateField()
    dateTransfer = models.DateField()
    dateComplaint = models.DateField()
