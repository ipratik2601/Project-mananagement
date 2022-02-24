from django.contrib import admin

from .models import Employee, Role, Student

# Register your models here.
admin.site.register(Role)
admin.site.register(Employee)
admin.site.register(Student)