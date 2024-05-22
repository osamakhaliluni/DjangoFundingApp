from django.urls import path
from .views import signIn, signUp, editProject, deleteProject, createProject, showProject, donateProject

urlpatterns=[
    path("", signIn, name="signin"),
    path("signup", signUp, name = "signup"),
    path('editproject/<title>/<user1>', editProject, name = "editproject"),
    path('deleteproject/<title>/<user1>', deleteProject, name = "deleteproject"),
    path('create/<user1>', createProject, name = "createproject"),
    path('showproject/<title>/<user1>', showProject, name = "showproject"),
    path('donateproject/<title>/<user1>', donateProject, name = "donateproject")
]