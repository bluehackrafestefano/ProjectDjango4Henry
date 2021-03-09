from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    # return HttpResponse("Hi from home page!")
    context = {
        'title': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4, 5]
    }
    return render(request, "fscohort/home.html", context)

def about(request):
    return HttpResponse("Hi from about page!")
