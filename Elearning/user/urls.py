from django.urls import path
from .views import *

urlpatterns = [
    path("Course/",CourseView.as_view(),name="Course"),
    path("Payment/",PaymentView.as_view(),name="Pay"),
    path('add/<int:cid>',addcourse,name='Add'),
    path('MyCourse/',MyCourseView.as_view(),name="My"),
    path('delCourse/<int:cid>',delcourse,name='Del'),
    
    ]
