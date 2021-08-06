from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the index.")


# enter to docker container with: docker exec -it DjangoProject /bin/bash
# hit command: python3 manage.py startapp django_exemple
# problem with privileges: sudo chown -c -R $USER:$USER (folder name)