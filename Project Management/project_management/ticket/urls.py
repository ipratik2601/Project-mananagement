from django import views
from django.urls import path, include
from .views import *
from ticket import views



urlpatterns = [
    path('add/',CreateTicket.as_view()),
    path('view/',ViewTicket.as_view()),
    path('<pk>/delete',DeleteTicket.as_view()),
    path('<pk>/update',UpdateTicket.as_view()),
    path('<pk>/detail',TicketDetail.as_view()),
]