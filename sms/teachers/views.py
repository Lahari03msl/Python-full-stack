from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('this is home')
def domain(request):
    return HttpResponse('this is domain')
def contact(request):
    return HttpResponse('this is contact')
def about(request):
    return HttpResponse('this is about')
def profile(request):
    return HttpResponse('this is profile')

