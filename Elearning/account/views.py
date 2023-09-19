from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,FormView,View
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistrationForm,UserLoginForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.

# Registration form
class SigninPage(CreateView):
    template_name="Reg.html"
    form_class= RegistrationForm
    model= User
    success_url=reverse_lazy('Homepage')


class LoginPage(FormView):
    template_name = "log.html"
    form_class = UserLoginForm
    def post(self,req,*args,**kwargs):
        form_data = UserLoginForm(data=req.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("username")
            pw=form_data.cleaned_data.get("password")
            auth=authenticate(req,username=un,password=pw)
            if auth:
                print(auth.username , "is logined")
                login(req,auth)
                messages.success(req,f"You logined as {auth.username}")
                return redirect("Course")
            else:
                print("here")
                messages.error(req,"Something went wrong , Please try again")
                return redirect("Homepage")
        else:
            return render(req,"login.html",{"form":form_data})




class LogOut(View):
    def get(self,req):
        logout(req)
        return redirect('Homepage')