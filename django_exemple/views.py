from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList, Item
# Create your views here.
def index(request, id):
    l = TodoList.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" % l )


# enter to docker container with: docker exec -it DjangoProject /bin/bash
# hit command: python3 manage.py startapp django_exemple
# problem with privileges: sudo chown -c -R $USER:$USER (folder name)