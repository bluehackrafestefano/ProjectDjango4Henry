from django.shortcuts import render
from django.http import HttpResponse
# from .forms import StudentForm
from .models import Student

def home_view(request):
    # return HttpResponse("Hi from home page!")
    
    # form = StudentForm()  # This renders an empty form of Students, but need to use it into a dictionary.
     
    # context = {
    #     'title': 'clarusway',
    #     'dict1': {'django': 'best framework'},
    #     'my_list': [2, 3, 4, 5],
    #     'form': form,
    # }
    # return render(request, "fscohort/home.html", context)

    return render(request, "fscohort/home.html")

# def about(request):
#     return HttpResponse("Hi from about page!")

def student_list(request):
    students = Student.objects.all()
    
    context = {
        'students': students
    }

    return render(request, "fscohort/student_list.html", context)