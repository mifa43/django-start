from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoList, Item
from .forms import CreateNewList
# Create your views here.
def index(response, id):
    #region how to use this ?
    #http://localhost:8001/<someName>   In order to do a search in the database, 
    # it is necessary to manually enter some information within the docker chontainer, which is explained in models.py
    #endregion
    l = TodoList.objects.get(id=id)
    
    return render(response, 'main/list.html', {"l": l})
def home(response):
    return render(response, 'main/home.html', {})

def create(response):
    if response.method == "POST": #capture POST method
        form = CreateNewList(response.POST) # 
        if form.is_valid(): #checking for valid inputs in form
            n = form.cleaned_data['name'] # delete data from inputs
            t = TodoList(name = n)  # adding items to db
            t.save()
        return HttpResponseRedirect("/%i" %t.id) #pass id and redirect to index
    else: # GET method
        form = CreateNewList()
    return render(response, 'main/create.html', {"form": form})
# enter to docker container with: docker exec -it DjangoProject /bin/bash
# hit command: python3 manage.py startapp django_exemple
# problem with privileges: sudo chown -c -R $USER:$USER (folder name)