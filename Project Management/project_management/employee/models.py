from django.db import models


# Create your models here.
class Employe(models.Model):
    employe_name = models.CharField(max_length=20)
    employe_email = models.EmailField()
    employe_age = models.IntegerField()
    employe_contact = models.CharField(max_length=50)
    class Meta:
        db_table = 'employe'
    