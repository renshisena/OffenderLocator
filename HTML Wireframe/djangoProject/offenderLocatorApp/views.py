from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from io import BytesIO

# Create your views here.

from django.http import HttpResponse, request
from .models import offenders1
from .forms import UserRegistration

#try print method


def user_registration(request):
    registerForm = UserRegistration()
    authcodes = request.POST.get('authorizationcode')
    authcode = 'admin123'
    if authcodes == authcode:
        if request.method == "POST":
            registerForm = UserRegistration(request.POST)
            print('WOW')
            if registerForm.is_valid():
                registerForm.save()
                return redirect('/login')

    context = {'registerForm':registerForm}
    return render(request,'htmlFiles/registration.html',context)

def homepage(request):
    return render(request, 'htmlFiles/homepage.html')

@login_required(login_url='/login')
def filecomplaint(request):
    return render(request, 'htmlFiles/filecomplaint.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('inputUsername')
        password =request.POST.get('inputLoginConfirm')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if username =='admin':
                login(request, user)
                return redirect('/account_manager') 
            else: 
                login(request, user)
                return redirect('/admin_lookup')
        else:
            messages.info(request, 'Username or password is incorrect.')
    context = {}
    return render(request, 'htmlFiles/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/login')

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
    
@login_required(login_url='/login')
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
def about(request):
    return render(request, 'htmlFiles/about.html')

@login_required(login_url='/login')
def accountmanager(request):
    barangayID = request.POST.get('getbarangayID')
    User.objects.filter(id=barangayID).delete()
    data = User.objects.all()
    context = {'data':data}
    return render(request,'htmlFiles/accountmanager.html',context)
