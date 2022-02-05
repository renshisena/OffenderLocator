from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.

from django.http import HttpResponse, request
from .models import offenders
from .models import offenders1

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
    offender = request.POST.get('inputName')
    age = request.POST.get('inputage')
    gender = request.POST.get('inputGender')
    offense = request.POST.get('inputoffense')
    casedescription = request.POST.get('inputcasedesc')
    offendertable = offenders1.objects.create(offender = offender, age=age, gender = gender, offense = offense, caseDescription = casedescription)
    offendertable.save()
    return redirect('/filecomplaint')


def showoffenders(request):
    data1 = offenders1.objects.all()
    return render(request, 'htmlFiles/lookup.html', {'data1':data1})