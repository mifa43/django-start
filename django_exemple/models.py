from django.db import models

# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length = 30)


    def __str__(self):
        return self.name
class Item(models.Model):
    artist = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    text = models.CharField(max_length=60)
    complete = models.BooleanField()
    def __str__(self):
        return self.text

#1. go to settings and add 'django_exemple.apps.DjangoExempleConfig' -/- dir_name.apps.class_name
#2. docker exec -it DjangoProject /bin/bash -/- python3 manage.py migrate
#3. create model in models.py after that do python3 manage.py makemigrations
#4. python3 manage.py migrate -/- after that a file should be created automatically
#5. python3 manage.py shell  :(InteractiveConsole) >>> 
#6. shell commands to write data in sqlite3:
# >>> from django_exemple.models import Item,TodoList
# >>> t = TodoList(name="Milos")
# >>> t.save()
# >>> TodoList.objects.all()
# <QuerySet [<TodoList: Milos>]>


#query: t = TodoList(name="Barbari") - insert
#       TodoList.objects.all() - select * from TodoList;
#       TodoList.objects.get(id=1) - select * from TodoList where id = 1;
# t.item_set.create(text="Hello world from docker-container!", complete=False) - way of writing values into a relation

#t.filter(name__startswith="Olivija") - filter comand
# delete method
# dell = t.get(id=1)
# dell.delete()
# returns (1, {'django_exemple.TodoList': 1})
