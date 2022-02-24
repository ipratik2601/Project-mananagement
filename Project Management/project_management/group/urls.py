from django.urls import path, include
from group import views


urlpatterns = [
    path('add/',views.group),
    path('contactus/',views.contactUs),
    path('aboutus/',views.aboutUs),
    path('',views.index),

    
]
