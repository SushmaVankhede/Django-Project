from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        "variable1":"This is Sushma",
        "variable2":"This is Hardik",
        "variable3":"This is Prisha"
    }
    # messages.success(request, "This is test message")
    return render(request, "index.html", context)
    #return HttpResponse("This is Home Page")
def aboutus(request):
    return render(request, "aboutus.html")
    # return HttpResponse("This is About UsPage")
def services(request):
    return render(request, "index.html")
    # return HttpResponse("This is Services Page") 
def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contactus = Contact(name = name,email = email, phone = phone, desc = desc, date = datetime.today() )
        contactus.save()
        messages.success(request, 'Your contact info has been sent !!!')

        

    return render(request, "contactus.html")
    # return HttpResponse("This is Contact Us Page")
