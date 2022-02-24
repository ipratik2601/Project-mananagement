from dataclasses import fields
from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import *
from .models import *
# Create your views here.
class CreateTicket(CreateView):
    model = Ticket
    fields = ['ticket_title','ticket_description']
    template_name = 'ticket/create_ticket.html'
    success_url = '/ticket/view/'

class ViewTicket(ListView):
    model = Ticket
    ticketlist = model.objects.all()
    template_name = 'ticket/view_ticket.html'
    context_object_name = 'ticketlist'

class DeleteTicket(DeleteView):
    model = Ticket
    success_url = '/ticket/view/'

class UpdateTicket(UpdateView):
    model = Ticket
    fields = ['ticket_title','ticket_description']
    template_name = 'ticket/update_ticket.html'
    success_url = '/ticket/view'
class TicketDetail(DetailView):
    model = Ticket
    template_name = 'ticket/ticket_detail.html'