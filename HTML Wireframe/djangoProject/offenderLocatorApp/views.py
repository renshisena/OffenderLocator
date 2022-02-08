from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.

from django.http import HttpResponse, request
from .models import *



def homepage(request):
    return render(request, 'htmlFiles/homepage.html')

def filecomplaint(request):
    return render(request, 'htmlFiles/filecomplaint.html')

def login(request):
    return render(request, 'htmlFiles/login.html')

def reset(request):
    return render(request, 'htmlFiles/forgot.html')

def lookup(request):
    data1 = offenders1.objects.all()
    context = {'data1':data1}
    return render(request, 'htmlFiles/lookup.html', context)
    

def adminlookup(request):
    janA1 = request.POST.get('caseStatus')
    janA2 = request.POST.get('getID')
    offenders1.objects.filter(id=janA2).update(caseStatus = janA1)
    data1 = offenders1.objects.all()
    context = {'data1':data1} 
    return render(request, 'htmlFiles/lookupAdmin.html',context)

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
    return redirect('/lookup')


    
def release(request):
     return render(request,'htmlFiles/release.html' )
def transfer(request):
     return render(request,'htmlFiles/transfer.html' )
def ongoing(request):
    return render(request,'htmlFiles/ongoing.html' )

# def viewdetails(request):
#     # offender_info = offenders1.objects.get(id=id)
    
#     print("w9io")
    # return redirect('/lookup')
def resetpassword(request):
    password = request.POST.get('inputResetPassword')
    newpassword = request.POST.get('inputResetConfirm')
    data = offenders2.objects(password=password).update(password = newpassword)
    return redirect('/login')
