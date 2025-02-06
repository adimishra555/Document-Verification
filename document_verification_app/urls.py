# document_verification_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('userdata', views.index, name='index'),
]
