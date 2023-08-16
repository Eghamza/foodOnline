from django.urls import path
from . import views

urlpatterns = [
    path('registervendor/', views.registervendor, name='registervendor'),
]
