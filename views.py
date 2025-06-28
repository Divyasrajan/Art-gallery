from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Categories,Download,About

def addhome(request):
    return render(request, 'hom.html')

def addabout(request):
    dec={
        'about': About.objects.all()
    }
    return render(request,'about.html', dec)

def addcategories(request):
    cat_name={
        'cat': Categories.objects.all()
    }
    return render(request,'categories.html', cat_name)

def adddownload(request):
      category= {
          'download':Download.objects.all()
      }
      return render(request,'download.html', category)

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages,auth

def loginpage(request): 
    if request.method == 'POST':
       usern = request.POST.get('username')
       passw = request.POST.get('password')

       user = authenticate(username=usern, password=passw)
       print(user)

       if user is not None:
           auth.login(request,user)
           return redirect('/')
       else:
           messages.info(request, 'invalid')
           return redirect('login')
    else:

      return render(request,'login.html')

def addlogout(request):
    auth.logout(request)
    return redirect('/')