from django.db import models

class Subject(models.Model):
    subject = models.CharField(max_length=50)
    abbrev = models.CharField(max_length=25)

    def __str__(self):
        return f"Subject name is {self.subject} Abbrev is {self.abbrev}"
        

