from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Course,MyCourse
from django.utils.decorators import method_decorator
from django.http import JsonResponse
import stripe
from django.contrib import messages



# Decorator
def signin_required(fn):
    def wrapper(req, *args, **kwargs):
        if req.user.is_authenticated:
            return fn(req, *args, **kwargs)
        else:
            return redirect("")
    return wrapper

# Create your views here.

@method_decorator(signin_required,name='dispatch')
class CourseView(TemplateView):
    template_name = "wtf.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_courses = Course.objects.all()
        my_courses = MyCourse.objects.filter(user=self.request.user).values_list('course', flat=True)
        available_courses = all_courses.exclude(id__in=my_courses)
        context['course'] = available_courses
        return context

class PaymentView(TemplateView):
    template_name= "payment.html"

    def create_payment_intent(request):
        amount = 1000  
        currency = 'usd'
        try:
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency=currency,
            )
            return JsonResponse({'clientSecret': intent.client_secret})
        except Exception as e:
            return JsonResponse({'error': str(e)})


def addcourse(request,*args,**kwargs):
    id=kwargs.get("cid")
    course=Course.objects.get(id=id)
    user=request.user
    if MyCourse.objects.filter(course=course,user=request.user):
        messages.warning(request,"Alredy Added")
        return redirect('Course')
    else:
        MyCourse.objects.create(course=course,user=user)
        messages.success(request,"Added")
        return redirect('Course')
    
def delcourse(request,*args,**kwargs):
    id=kwargs.get("cid")
    user=request.user
    MyCourse.objects.filter(id=id).delete()
    messages.error(request,"Item Removed form MyCourse")
    return redirect('My')

@method_decorator(signin_required,name='dispatch') 
class MyCourseView(TemplateView):
    template_name = "mycourse.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course"] = MyCourse.objects.filter(user=self.request.user)
        return context