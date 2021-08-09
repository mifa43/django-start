from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm #this is a module that we call from djanga it will provide us with an already automatically created registration form
# Create your views here.
def register(response):
    form = UserCreationForm()
    return render(response, "main/register.html", {"form": form})   #calling template and rendering django form
    