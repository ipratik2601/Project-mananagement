from django.urls import URLPattern, path
from .views import *

urlpatterns = [
    path('add/',CreateTask.as_view()),
    #path('view/',),
]