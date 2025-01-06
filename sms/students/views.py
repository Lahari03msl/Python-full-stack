from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Student

# Create your views here.
def home(request):
    return HttpResponse('this is home')
def course(request):
    return HttpResponse('this is course')
def contact(request):
    return HttpResponse('this is contact')
def about(request):
    return HttpResponse('this is about')
def profile(request):
    return render(request,'test.html')
def prints(request):
    students = Student.objects.all()
    return render(request,'test1.html',{'std':students})