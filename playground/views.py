from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# is a request handler
# takes request -> response

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Isaac'})