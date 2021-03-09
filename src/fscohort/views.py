from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Hi from home page!")

def about(request):
    return HttpResponse("Hi from about page!")
