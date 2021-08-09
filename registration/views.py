from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm #this is a module that we call from djanga it will provide us with an already automatically created registration form
# Create your views here.
def register(response):
    if response.method == "POST":   #we catch a post request 
        form = UserCreationForm(response.POST)
        if form.is_valid(): # if form input is valid we add the user and store in the database and redirect to the home page
            form.save()
        return redirect("/home")
    else:   #showing only a blank form
        form = UserCreationForm()
    return render(response, "main/register.html", {"form": form})   #calling template and rendering django form
    