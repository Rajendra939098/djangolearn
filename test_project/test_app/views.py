from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'test_app/home.html')

def blog(request):
    return render(request,"test_app/blog.html")

def login(request):
    return render(request,'test_app/login.html')
def register(request):
    return render(request,'test_app/register.html')