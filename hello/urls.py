from django.urls import path
from . import views

urlpatterns = [
    #when hello.urls is running, set default path to index function
    path("", views.index, name="index"),

    #otherwise:
    path("khong", views.khong, name="khong"),
    path("iris", views.iris, name="iris"),

    #for dynamic string insertion
    path("<str:name>", views.greet, name="name")

    #view.something means access a function in views.py of this application
]