from datetime import date
from distutils.command.upload import upload
from operator import truediv
from os import link
from pickle import NONE
from turtle import title
from unicodedata import name
from django.db import models
from django.forms import EmailField

# Create your models here.
class Home (models.Model):
    title=models.CharField(max_length=250)
    text=models.TextField()
    date= models.DateField()
    image = models.ImageField(blank=True, upload_to="images/")
    url=models.URLField(max_length=300, null=True)
    
   

    def __str__(self):
        return self.title


    




















































        return self.title