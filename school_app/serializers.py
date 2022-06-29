from dataclasses import fields
from rest_framework import serializers

from school_app import models
class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Student
        fields= "__all__"
    