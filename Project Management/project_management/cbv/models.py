from django.db import models

# Create your models here.
class Hr(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.IntegerField()
    class Meta:
        db_table = 'hr'