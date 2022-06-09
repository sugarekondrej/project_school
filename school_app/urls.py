from django.urls import path
from . import views

urlpatterns = [
    path ("hello-world",views.hello_world,name="hello"),
    path("subjects",views.print_subjectst,name="subject0_list"),
    path("subjects/<int:pk>",views.subject_detail,name="sub_detail")
]
