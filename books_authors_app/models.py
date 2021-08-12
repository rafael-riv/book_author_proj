from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=255)
    desc  = models.TextField()
    create_ad = models.DateTimeField(auto_now_add= True )
    update_ad = models.DateTimeField(auto_now_add= True)
    # authors
    def __repr__(self) -> str:
        return f'{self.id} : {self.title}'

class Author(models.Model):
    firt_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notas = models.TextField(default='hola')
    books = models.ManyToManyField(Books, related_name="authors")
    create_ad = models.DateTimeField(auto_now_add= True )
    update_ad = models.DateTimeField(auto_now_add= True)
    def __repr__(self) -> str:
        return f'{self.id} : {self.firt_name}'
