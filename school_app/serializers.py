from rest_framework import serializers

from school_app import models
class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"