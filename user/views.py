from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from .models import Developer,CustomUser
import requests

def home(request):
    response = requests.get("https://api.rootnet.in/covid19-in/stats/latest").json()
    return render(request,'user/home.html',{'response':response})

def cases(request):
    response = requests.get("https://api.rootnet.in/covid19-in/stats/latest").json()
    return render(request,'user/cases_display.html',{'response':response})

def beds(request):
    response = requests.get("https://api.rootnet.in/covid19-in/hospitals/medical-colleges").json()
    return render(request,'user/hospital_beds.html',{'response':response})

def about(request):
    dev=Developer.objects.all()
    context={
        'dev':dev
    }
    return render(request,'user/about.html',context)

def contact(request):
    return render(request,'user/contact.html')

def signup(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'user/signup.html',{'form':form})


def info(request):
    response1 = requests.get("https://api.rootnet.in/covid19-in/stats/latest").json()
    response2 = requests.get("https://api.rootnet.in/covid19-in/hospitals/medical-colleges").json()
    user=CustomUser.objects.get(id=request.user.id)
    context={
        'res1':response1,
        'res2':response2,
        'user':user,
    }
    return render(request,'user/necessary_info.html',context)