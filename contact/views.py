from django.shortcuts import render
from .models import  contact
# Create your views here.

def ContactUs(request):
    if request.method== 'POST':
     #1 get data from form:
      v_name= request.POST.get('field1')
      v_email= request.POST.get('field2')
      v_msg= request.POST.get('field3')
      #2 send data to DB
      v_contact = contact(name= v_name, mail= v_email, text=v_msg)
      v_contact.save()
      return render( request, 'contact/thank.html')
        
    else:
     return render(request,'contact/contactus.html')