from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Trends

def display(request):
    vals = Trends.objects.all()
    return render(request,'test2.html',{'i':vals})

# Create your views here.
