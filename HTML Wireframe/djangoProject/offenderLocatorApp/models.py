from pickle import FALSE, TRUE
from tabnanny import verbose
from django.db import models
from datetime import datetime


from django.forms import CharField, DateField, IntegerField
from django.utils import timezone


# Create your models here.


class offenders1(models.Model):
    status = (
        ("Ongoing","Ongoing"),
        ("Released","Released"),
        ("Transferred","Transferred"),
    )
    complainant = models.CharField(max_length=45, verbose_name='complainant',null=TRUE)
    complainantEmail = models.EmailField(null=FALSE)
    offender = models.CharField(max_length=45, verbose_name='offender')
    gender = models.CharField(max_length=6, verbose_name='gender')
    age = models.IntegerField()
    offense = models.CharField(max_length=45, verbose_name='offense')
    caseStatus = models.CharField(max_length=11, choices=status, default='Ongoing')
    caseDescription = models.TextField(max_length = 400,null = TRUE,verbose_name='caseDescription')
    offenderPic = models.ImageField(null=TRUE, blank = TRUE,upload_to='static/Media/')
    datenow = models.CharField(max_length = 45,verbose_name='datenow',null=FALSE)
    dateSchedule = models.CharField(max_length = 45,verbose_name='dateSchedule',null=TRUE)
    timeSchedule = models.CharField(max_length = 45,verbose_name='timeSchedule',null=TRUE)