from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
def registration(request):
    EUMFO=UserMF()
    EPMFO=ProfileMF()
    d={"EUMFO":EUMFO,"EPMFO":EPMFO}

    if request.method=="POST" and request.FILES:
        NMUSMFDO=UserMF(request.POST)
        NMPMFDO=ProfileMF(request.POST,request.FILES)
        if NMUSMFDO.is_valid() and NMPMFDO.is_valid():
            MUSMFDO=NMUSMFDO.save(commit=False)
            password=NMUSMFDO.cleaned_data['password']
            MUSMFDO.set_password(password)
            MUSMFDO.save()



            MPMFDO=NMPMFDO.save(commit=False)
            MPMFDO.user_name=MUSMFDO
            MPMFDO.save()
            send_mail('registration','Thanks for registration','saishankareddykarri@gmail.com',
            [MUSMFDO.email],
            fail_silently=False)
            return HttpResponse("Registration is successfull")
        else:
            return HttpResponse("Invalid Data")

    return render(request,'registration.html',d)

def home(request):
    return render(request,'home.html')

def user_login(request):
    return render(request,'user_login.html')