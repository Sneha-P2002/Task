from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Course


# Decorator
def signin_required(fn):
    def wrapper(req, *args, **kwargs):
        if req.user.is_authenticated:
            return fn(req, *args, **kwargs)
        else:
            return redirect("Homepage")
    return wrapper

# Create your views here.


class CourseView(TemplateView):
    template_name = "wtf.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course"] = Course.objects.all()
        return context
