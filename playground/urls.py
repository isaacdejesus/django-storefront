from django.urls import path
from . import views
#This is a URLCONF. every app can have own URLCONF
#Need to import this URLCONF into the main project's URLCONF
urlpatterns = [
    path('hello/', views.say_hello)
]