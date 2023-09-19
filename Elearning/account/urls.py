from django.urls import path
from .views import *

urlpatterns = [
    path("Reg/",SigninPage.as_view(),name="SignUp"),
    path('Logout',LogOut.as_view(),name="logout")
]