from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "hello_world/index.html")


def about(request):
    return render(request, "hello_world/about.html")


def contact(request):
    return HttpResponse("This is a contact page!")
