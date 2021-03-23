from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.


def index(request):

    # return HttpResponse("Home || This is testing site!!!")
    #messages.success(request, "this is a test message")
    return render(request, 'index.html')


def about(request):
    # return HttpResponse("about page")
    return render(request, 'about.html')


def services(request):
    # return HttpResponse("services page")
    return render(request, 'services.html')


def contact(request):
    # return HttpResponse("contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())

        contact.save()
        messages.success(request, 'Your message has been sent. ')
    return render(request, 'contact.html')
