from . import views

from django.urls import path


urlpatterns = [
path('contactus',views.ContactUs,name='contactus')
]