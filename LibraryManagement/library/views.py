from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render (request, 'library/index.html')

def aboutus(request):
    return  render (request, 'library/aboutus.html')
    
def services(request):
    return  render (request, 'library/services.html')

def signup(request):
    return  render (request, 'library/signup.html')

def login(request):
    return  render (request, 'library/login.html')

def forgetpw(request):
    return  render (request, 'library/forgetpw.html')