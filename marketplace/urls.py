from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.listing, name='marketplace'),
    path('<slug:slug>/', views.vendordetail, name='vendor_detail'),

    #add_to_cart
    path('add_to_cart/<int:food_id>/', views.add_to_cart, name='add_to_cart'),
    #dicrease car
    path('dicrease_cart/<int:food_id>/', views.dicrease_cart, name='dicrease_cart'),

    #delete_cart
    path('delete_cart/<int:cart_id>/', views.delete_cart,name='delete_cart')
]