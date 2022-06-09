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
