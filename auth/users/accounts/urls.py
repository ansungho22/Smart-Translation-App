from django.urls import path, include
from . import views

urlpatterns = [
    path("signup/", views.signup),
    path("login/", views.login),
    path("delete/", views.delete),
    path("update/", views.update),
]
