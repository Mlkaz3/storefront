# map urls to the view function 
from django.urls import path 
from . import views 
# to reference view function 

urlpatterns = [
    path('hello/', views.say_hello)
]



