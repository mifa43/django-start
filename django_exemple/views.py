from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoList, Item
from .forms import CreateNewList
# Create your views here.
def index(response, id):
    #region how to use this ?
    #http://localhost:8001/<someName>   In order to do a search in the database, 
    # it is necessary to manually enter some information within the docker container, which is explained in models.py
    #endregion
    l = TodoList.objects.get(id=id)
    #region explanation
    # costume form
    # the goal is to automatically update the complete value in the database, 
    # if the check box is pressed the value in the database will be saved after pressing the save button and the value in the database will be upgraded,
    # if we enter a value in the text input field and press the add new item button the complete value is False by default and both values are added to the database
    #endregion
    if response.method == 'POST':
        print(response.POST)
        if response.POST.get("save"):
            for item in l.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                l.item_set.create(text=txt, complete=False) #default value is False
            else:
                print("invalid actions!")
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