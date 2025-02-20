from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
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
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')

def user_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO:
            if AUO.is_active:
                login(request,AUO)
                request.session['username']=username
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Not a active user")
        else:
            return HttpResponse("Invalid credentials")
    return render(request,'user_login.html')
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
@login_required
def profile_display(request):
    USN=request.session.get('username')
    UO=User.objects.get(username=USN)
    PO=Profile.objects.get(user_name=UO)
    d={'UO':UO,'PO':PO}
    return render(request,'profile_display.html',d)


@login_required
def change_password(request):
    if request.method=='POST':
        USN=request.session.get('username')
        UO=User.objects.get(username=USN)
        NP=request.POST['np']
        UO.set_password(NP)
        UO.save()
        return HttpResponse('password is changed successfully')
    return render(request,'change_password.html')
























