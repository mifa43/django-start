from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList, Item

# Create your views here.

def index(request, name):
    #region how to use this ?
    #http://localhost:8001/<someName>   In order to do a search in the database, 
    # it is necessary to manually enter some information within the docker chontainer, which is explained in models.py
    #endregion
    l = TodoList.objects.get(name=name)
    item = l.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br></br><h1>%s</h1>" % (l.name, str(item.text)) )


# enter to docker container with: docker exec -it DjangoProject /bin/bash
# hit command: python3 manage.py startapp django_exemple
# problem with privileges: sudo chown -c -R $USER:$USER (folder name)