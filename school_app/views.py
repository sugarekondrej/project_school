from hashlib import new
from pyexpat import model
from urllib import request
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from school_app import models
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict



from school_app import serializers
from rest_framework import viewsets

class BookViewsets(viewsets.ModelViewSet):
    serializer_class = serializers.BookSerializers
    queryset = models.Book.objects.all()






@csrf_exempt
def print_teachers(request):
    if request.method =="GET":
        teachers = list(models.Teachers.objects.values())
        return JsonResponse(teachers,safe = False,status=200)
    elif request.method =="POST":
        teacher_bytes = request.body
        new_teacher_body=json.loads(teacher_bytes)
        new_teacher = models.Teachers(**new_teacher_body)
        new_teacher.save()
        return JsonResponse(new_teacher_body,status=200)
@csrf_exempt  
def teachers_details(request,pk):
    teacher = (models.Teachers.objects.get(pk=pk))
    if request.method == "GET":
        return JsonResponse(model_to_dict(teacher))
    elif request.method == "PUT":
        put_body_bytes = request.body
        new_translate = json.loads(put_body_bytes)
        teacher.__dict__.update(new_translate)
        teacher.save()
        return JsonResponse(new_translate, status = 200)
    elif request.method == "DELETE":
        teacher.delete()
        return HttpResponse("Succesfully deleted")


@csrf_exempt  
def print_subjectst(request):
    if request.method == "GET":
        subjects = list(models.Subject.objects.values())
        return JsonResponse(subjects, safe=False, status=200)
    
    elif request.method == "POST":
        subject=request.body
        subject_dist = json.loads(subject)
        new_subject=models.Subject(**subject_dist)
        new_subject.save()
        return JsonResponse(subject_dist)
# podle indexu v IRL        
@csrf_exempt
def subject_detail(request,pk):
    try:
        subject = models.Subject.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse("There is no subject id with" + id, status = 404)
    if request.method == "GET":
       return JsonResponse(model_to_dict(subject))
    #update na indexu který vybereme pomoci URL
    elif request.method =="PUT":
        newsubject_bytes = request.body
        new_subject = json.loads(newsubject_bytes)
        subject.__dict__.update(new_subject)
        subject.save()
        
        return JsonResponse(new_subject, status = 201)
    elif request.method =="DELETE":
        subject.delete()
        return HttpResponse("No content")

