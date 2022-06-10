from pyexpat import model
from unicodedata import name
from django.db import models
from django.forms import CharField

class Subject(models.Model):
    subject = models.CharField(max_length=50)
    abbrev = models.CharField(max_length=25)

    def __str__(self):
        return f"Subject name is {self.subject} Abbrev is {self.abbrev}"
        

class Teachers(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    

    def __str__(self):
        return f"Name of techaer is: {self.name} and Subject is: {self.subject}"
class Book(models.Model):
    name = models.CharField(max_length=30)
    title=models.CharField(max_length=50)
    subject = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["created"]
    def __str__(self):
        return f"Name is {self.name} title is: {self.title} and subject is: {self.subject}"
