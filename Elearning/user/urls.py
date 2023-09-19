from django.urls import path
from .views import *

urlpatterns = [
    path("Course/",CourseView.as_view(),name="Course")
]