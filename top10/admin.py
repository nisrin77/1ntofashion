from django.contrib import admin

from top10.views import topt10

# Register your models here.
from .models import topt10
admin.site.register(topt10)