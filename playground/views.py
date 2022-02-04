from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
# request -> response 
# request handler 
# action 

# create first view function
# the function will take a request object
# return a response 
# it needs to be map to url
def say_hello(request):
    # pull data from db, tarnsform, send email
    return HttpResponse('Hello World')