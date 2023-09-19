from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'email',
            'username',
            'password1','password2'
            
        ]

class UserLoginForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput())
    password=forms.CharField(max_length=100,widget=forms.TextInput())