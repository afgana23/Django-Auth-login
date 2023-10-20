import dataclasses
from urllib import request
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from DbModel.models import Country
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def home (request):
        if request.method=='POST':
                username=request.POST['username']
                password=request.POST['password']
                user=authenticate(request,username=username,password=password)
                if user is not None:
                        login(request,user)
                        messages.success(request,"logged in")
                        return redirect('home')
                else:
                        messages.success(request,"eroor somrthing wrong")
                        return redirect('home')
        else:
         return render(request,"home.html")

def savecountry(request):
        n=''
        if request.method=='POST':

               cname=request.POST.get('cname')
               ad=Country(country_name=cname) 
               ad.save()
               n="data inserted"

        return render(request,"home.html",{'n':n})


def login_user(request):
        pass
def logout_user(request):
        logout(request)
        messages.success(request,"You havebeen logout")
        return redirect('home')
       
def about(request):
        
        dbdata=Country.objects.all()
        data={
                "dbdata":dbdata
        }
       
        return render(request,"about.html",data)