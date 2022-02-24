from django.db import models

# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=50)
    role_description = models.TextField()
    class Meta:
        db_table = 'role'


class Employee(Role):
    employee_name = models.CharField(max_length=50)
    employee_email = models.CharField(max_length=50)
    employee_password = models.CharField(max_length=50)
    employee_phone = models.CharField(max_length=50)
    employee_address = models.TextField()
    employee_dob = models.DateField()

    class Meta:
        db_table = 'employee'

class Student(models.Model):
    role_id = models.OneToOneField(Role,on_delete=models.CASCADE,null=True)
 #one to many relation  # role_id = models.ForeignKey(Role,on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50)
    student_email = models.CharField(max_length=50)
    student_password = models.CharField(max_length=50)
    student_phone = models.CharField(max_length=50)
    student_address = models.CharField(max_length=50)
    student_dob = models.DateField()

    class Meta:
        db_table = 'student'

    