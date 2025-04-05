from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index():
    return HttpResponse("Hello, World")


def about(request):
    return render(request, "hello_world/about.html")


def contact():
    return HttpResponse("This is a contact page!")
