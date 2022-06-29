from django.urls import path
from . import views
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("books",views.BookViewsets)
router.register("students",views.StudentViewsets)

urlpatterns = [
   
    path("subjects",views.print_subjectst,name="subject0_list"),
    path("subjects/<int:pk>",views.subject_detail,name="sub_detail"),
    path("teachers",views.print_teachers,name="teach"),
    path("teachers/<int:pk>", views.teachers_details,name="teach_details"),
    path("",include(router.urls)),
]
