from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import contact

# Create your views here.
def index(request):
    context = {
        # "variable1":"I am the best",
        # "variable2":"and more thing hard"
    }
    return render(request,'index.html',context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request,'about.html')
    # return HttpResponse("this is about page")

def services(request):
    return render(request,'services.html')
    # return HttpResponse("this is services page")

def contact(request):
    if request.method=="post":
        name = request.POST.get('Name')
        phone = request.POST.get('Phone')
        email = request.POST.get('Email')
        desc = request.POST.get('desc')
        contact = contact(name=Name,phone=Phone,email=Email,desc=desc,date=datetime.today())
        contact.save()

    return render(request,'contact.html')
    # return HttpResponse("this is contact page")