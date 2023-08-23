from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='vprofile'),
    path('menu_builder/', views.menu_builder, name='menu_builder'),
]
