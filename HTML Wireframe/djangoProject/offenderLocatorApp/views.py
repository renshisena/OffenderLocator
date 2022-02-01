from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, request

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

def admin(request):
    return render(request, 'htmlFiles/lookupAdmin.html')