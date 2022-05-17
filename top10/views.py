from django.shortcuts import render
from .models import topt10
# Create your views here.
def Top10(request):
    post =topt10.objects.all()
    return render(request,'Top10/trends.html',{'post':post})