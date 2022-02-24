from multiprocessing import context
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def group(request):
    return HttpResponse(' group called........')

def index(request):
    context ={
        'name':'FLIPKART',
    }
    return render(request,'group/index.html',context)

def contactUs(request):
    context = {
        'contact_name':["pratik","ashmita","rajesh","suresh","jatin"]
    }
    return render(request,'group/contactus.html',context)

def aboutUs(request):
    context = {
         ' isActive' : False,
         'age': 19,

    }
    return render(request,'group/aboutus.html',context)