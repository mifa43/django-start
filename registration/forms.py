from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm #this is a module that we call from djanga it will provide us with an already automatically created registration form
from django import forms
from django.contrib.auth.models import User
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()  #setting the registration form to receive an email field

    class Meta: # we say that the new form model is stored in the user database
        model = User
        fields = ["username", "email", "password1", "password2"]    #expressions of the field in which order they will be displayed on the screen
        #this is very important, to add a new field that has been created to be displayed in the form