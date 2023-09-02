from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.listing, name='marketplace'),
    path('<slug:slug>/', views.vendordetail, name='vendor_detail'),

    path('add_to_cart/<int:food_id>')
]