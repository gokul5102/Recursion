from django.shortcuts import render
from django.http import HttpResponse
import requests

def home(request):
    return render(request,'user/home.html')

def cases(request):
    response = requests.get("https://api.rootnet.in/covid19-in/stats/latest").json()
    return render(request,'user/cases_display.html',{'response':response})

def beds(request):
    response = requests.get("https://api.rootnet.in/covid19-in/hospitals/medical-colleges").json()
    return render(request,'user/hospital_beds.html',{'response':response})

def about(request):
    return render(request,'user/about.html')

def contact(request):
    return render(request,'user/contact.html')
