from django.shortcuts import render,redirect
# password for test user is Karan@123
# Create your views here.
def index(request):
    render(request,'index.html')

def login(request):
    render(request,'login.html')

def logout(request):
    render(request,'index.html')

