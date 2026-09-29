from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll_no = request.POST.get('roll_no')
        course = request.POST.get('course')
        email = request.POST.get('email')
        Student.objects.create(name=name, roll_no=roll_no, course=course, email=email)
        return redirect('student_list')
    return render(request, 'students/add_student.html')