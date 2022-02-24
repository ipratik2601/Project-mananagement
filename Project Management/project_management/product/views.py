from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def addProduct(request):
    print('ADD PRODUCT CALL')
    return HttpResponse('addProduct called ........')

# view product function
def viewProduct(request):
    return HttpResponse('viewProduct called .........')

# product page shows the html page
def productpage(request):
    return render(request , 'product/productpage.html')

#contactus
def contactUS(request):
    return render(request ,'product/contactus.html' )

#aboutus
def aboutUs(request):
    return render(request , 'product/aboutus.html')

