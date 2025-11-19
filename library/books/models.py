from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250) 
    author = models.CharField(max_length=100) 
    isbn = models.CharField(max_length=13)

    def __str__(self):        # a __str__ method so that the title of a book will display in readable format in the admin later on
        return self.title