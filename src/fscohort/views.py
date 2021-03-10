from django.shortcuts import get_object_or_404, render, redirect
# from django.http import HttpResponse
from .forms import StudentForm
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

def student_add(request):
    # First need to show an empty form of Students
    form = StudentForm()  # Bring the student form, it will be empty
    if request.method == "POST":
        print(request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'form': form
    }
    return render(request, "fscohort/student_add.html", context)

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    # student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, "fscohort/student_detail.html", context)

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    return render(request, "fscohort/student_delete.html")

def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    # student = Student.objects.get(id=id)  # Select the student with id
    form = StudentForm(instance=student)  # Bring the student form, it will be filled with student
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'student': student,
        'form': form,
    }
    return render(request, 'fscohort/student_update.html', context)