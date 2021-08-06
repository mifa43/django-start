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
#4. python3 manage.py migrate -/- after that a fail should be created automatically
#5. python3 manage.py shell  :(InteractiveConsole) >>> 
