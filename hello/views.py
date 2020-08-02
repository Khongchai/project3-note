from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def khong(request):
    return HttpResponse("Hello, Khong")

def iris(request):
    return HttpResponse("Hello, Iris")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")

    