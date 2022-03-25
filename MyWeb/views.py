from django.shortcuts import render
from time import strftime
from django.core.mail import send_mail
# Create your views here.
def home(request):
    
    return render(request,"MyWeb/index.html")
    