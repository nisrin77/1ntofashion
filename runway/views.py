from django.shortcuts import render
from .models import show
# Create your views here.
def runway(request):
    post=show.objects.all()
    return render (request,'runway/22runway.html',{'post':post})