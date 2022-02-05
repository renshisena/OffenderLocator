from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, request
from .models import offenders

def homepage(request):
    return render(request, 'htmlFiles/homepage.html')

def filecomplaint(request):
    return render(request, 'htmlFiles/filecomplaint.html')

def login(request):
    return render(request, 'htmlFiles/login.html')

def reset(request):
    return render(request, 'htmlFiles/forgot.html')

def lookup(request):
    return render(request, 'htmlFiles/lookup.html')

def adminlookup(request):
    return render(request, 'htmlFiles/lookupAdmin.html')

def results(request):
    return render(request, 'htmlFiles/results.html')


def addoffender(request):
    offender = request.POST["inputname"]
    inputsurname = request.POST["inputsurname"]
    age = request.POST["inputage"]
    gender = request.POST["inputgender"]
    offense = request.POST["inputoffense"]
    caseDescription = request.POST["inputcasedesc"]
    
    offendertable = offenders(offender = offender,inputsurname=inputsurname, inputage=age, inputgender = gender, offense = offense, caseDescription = caseDescription)
    
    offendertable.save()
    return render(request, "htmlFiles/results.html")

def showoffenders(request):
    pass