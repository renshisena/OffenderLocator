from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

from django.http import HttpResponse, request
from .models import *

def user_registration(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #wala pang method
            return redirect()
    context = {
        'form':form
    }
    return render(request,'htmlFiles/lookupAdmin.html',context)
def homepage(request):
    return render(request, 'htmlFiles/homepage.html')

def filecomplaint(request):
    return render(request, 'htmlFiles/filecomplaint.html')

def login(request):
    return render(request,'htmlFiles/login.html')

def view_details(request):
    return render(request,'htmlFiles/viewdatails.html')

def lookup(request):
    data1 = offenders1.objects.all()
    context = {'data1':data1}
    
    if request.method == 'POST':
        id = request.POST.get('submitBtn')
        tableoff = offenders1.objects.filter(id=id)
        context = {'tableoff':tableoff}
        return render(request, 'htmlFiles/viewdetails.html', context)
    return render(request, 'htmlFiles/lookup.html', context)
    


def adminlookup(request):
    janA1 = request.POST.get('caseStatus')
    janA2 = request.POST.get('getID')
    offenders1.objects.filter(id=janA2).update(caseStatus = janA1)
    data1 = offenders1.objects.all()
    context = {'data1':data1}
    return render(request, 'htmlFiles/lookupAdmin.html',context)

def addoffender(request):
    offender = request.POST.get('inputName')
    age = request.POST.get('inputage')
    gender = request.POST.get('selectedGender')
    offense = request.POST.get('inputoffense')
    today=date.today()
    casedescription = request.POST.get('inputcasedesc')
    offendertable = offenders1.objects.create(offender = offender, age=age, gender = gender, offense = offense, caseDescription = casedescription, datenow = today)
    offendertable.save()
    return redirect('/lookup')
 
def release(request):
     return render(request,'htmlFiles/release.html' )
def transfer(request):
     return render(request,'htmlFiles/transfer.html' )
def ongoing(request):
    return render(request,'htmlFiles/ongoing.html' )

def registration(request):
    return render(request, 'htmlFiles/registration.html')
def records(request):
    return render(request, 'htmlFiles/records.html')