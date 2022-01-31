from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, request

def welcome(request):
    return render(request, 'htmlFiles/welcome.html')

def filecomplaint(request):
    return render(request, 'htmlFiles/filecomplaint.html')

def login(request):
    return render(request, 'htmlFiles/login.html')

def reset(request):
    return render(request, 'htmlFiles/forgot.html')

def lookup(request):
    return render(request, 'htmlFiles/lookup.html')

