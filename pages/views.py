from django.shortcuts import render
from django.http import HttpResponse
from .models import Home 
# Create your views here.
def home(request):
    post=Home.objects.all()
    return render (request,'pages/Home.html',{'post':post})

def about(request):
    return render (request,'pages/about.html')




