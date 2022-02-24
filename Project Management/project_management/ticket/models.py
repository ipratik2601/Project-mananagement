from django.db import models

# Create your models here.
class Ticket(models.Model):
    ticket_title = models.CharField(max_length=50)
    ticket_description = models.TextField()
    class Meta:
        db_table = 'ticket'
        