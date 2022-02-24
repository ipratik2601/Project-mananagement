from django.contrib import admin
from django.urls import path, include
from product import views



urlpatterns = [
    path('addproduct/',views.addProduct),
    path('viewproduct/',views.viewProduct),
    path('',views.productpage),
    path('contactUs/',views.contactUS),
    path('aboutUs/',views.aboutUs),


    
]
