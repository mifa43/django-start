from django.shortcuts import render, redirect
from .forms import RegistrationForm
# Create your views here.
def register(response):
    if response.method == "POST":   #we catch a post request 
        form = RegistrationForm(response.POST)
        if form.is_valid(): # if form input is valid we add the user and store in the database and redirect to the home page
            form.save()
        return redirect("/home")
    else:   #showing only a blank form
        form = RegistrationForm()
    return render(response, "main/register.html", {"form": form})   #calling template and rendering django form
    