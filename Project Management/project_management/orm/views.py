from multiprocessing import context
from django.shortcuts import render
from .models import Student

# Create your views here.
def studentData(request):

    students = Student.objects.all()
   # students1 = Student.objects.filter(student_name__startswith='x')

    context = {
        'students':students
    }

    return render(request,'orm/student.html',context)