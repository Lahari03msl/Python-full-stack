from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Gadgets

def display(request):
    vals = Gadgets.objects.all()
    return render(request,'test1.html',{'i':vals})

# Create your views here.
