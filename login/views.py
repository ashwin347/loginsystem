from django.shortcuts import render
from django.http import HttpResponse
from login.models import userdata
# Create your views here.
def home(request):
    return render(request,'login.html',{"data":"","color":"white"});

def validate(request):
    username=request.GET['username']
    passw=request.GET['password']
    user=userdata.objects.filter(name=username,password=passw)
    if len(user)==0:
    #if username=='ashwin' and passw=='babu':
        return render(request,'login.html',{"data":'username or password incorrect',"color":"red"})
    else:
        return render(request,'login.html',{"data":'login successfull',"color":"green"})
def signup(request):
    username=request.GET['username']
    passw=request.GET['password']
    entry=userdata(name=username,password=passw)
    entry.save()
    return render(request,'login.html',{"data":'signup successfull',"color":"green"})
    