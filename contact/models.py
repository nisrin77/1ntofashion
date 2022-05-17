from django.db import models

# Create your models here.
class contact(models.Model):
    text=models.TextField()
    mail=models.EmailField()
    name=models.CharField(max_length=200, null=True)