from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from .models import Employe

# Create your views here.
def addEmployee(request):
    emp = Employe(employe_name = 'Johnny',employe_email = 'Johnny@gmail.com',employe_age = 25,employe_contact = 7284808180)
    emp.save()
    return HttpResponse("Employee added.......")

def viewEmployee(request):
    emp = Employe.objects.all()
    context = {
        'employe':emp
    }
  # print(employe)
    return render(request,'employee/view.html',context)

def deleteEmployee(request):
    emp = Employe.objects.get(id=2)
    emp.delete()
    return HttpResponse("Employee Deleted.....")

def updateEmployee(request):
    emp = Employe.objects.get(id=3)
    emp.employe_contact = 9898450350
    emp.employe_name = 'Robert'
    emp.employe_email = 'Robert@gmail.com'
    emp.save()
    return HttpResponse("Employee Updated .......")
