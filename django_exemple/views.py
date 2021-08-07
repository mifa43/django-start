from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList, Item
from .forms import CreateNewList
# Create your views here.
def index(request, id):
    #region how to use this ?
    #http://localhost:8001/<someName>   In order to do a search in the database, 
    # it is necessary to manually enter some information within the docker chontainer, which is explained in models.py
    #endregion
    l = TodoList.objects.get(id=id)
    
    return render(request, 'main/list.html', {"l": l})
def home(request):
    return render(request, 'main/home.html', {})

def create(request):
    form = CreateNewList()
    return render(request, 'main/create.html', {"form": form})
# enter to docker container with: docker exec -it DjangoProject /bin/bash
# hit command: python3 manage.py startapp django_exemple
# problem with privileges: sudo chown -c -R $USER:$USER (folder name)