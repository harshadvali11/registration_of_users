from django import forms
from app.models import *
class UserMF(forms.ModelForm):
    class Meta:
        model=User
        #fields='__all__'
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}


class ProfileMF(forms.ModelForm):
    class Meta:
        model=Profile
        #fields='__all__'
        fields=['address','profile_pic']
