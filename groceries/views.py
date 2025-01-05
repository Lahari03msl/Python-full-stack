from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Items

def display(request):
    vals = Items.objects.all()
    return render(request,'test3.html',{'i':vals})

# Create your views here.
