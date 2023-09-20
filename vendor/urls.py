from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='vprofile'),
    path('menu_builder/', views.menu_builder, name='menu_builder'),
    path('food_item_category/<int:pk>',views.food_item_category, name='food_item_category'),



    #category crud
    path('menu_builder/category/add', views.add_category, name='add_category'),
    path('menu_builder/category/edit/<int:pk>', views.edit_category, name='edit_category'),
    path('menu_builder/category/delete/<int:pk>', views.delete_category, name='delete_category'),

    #food item 
    path('menu_builder/food/add', views.add_food, name='add_food'),
    path('menu_builder/food/edit/<int:pk>', views.edit_food, name='edit_food'),
    path('menu_builder/food/delete/<int:pk>', views.delete_food, name='delete_food'),

    #opening hours crud

    path('opening_hours', views.opening_hours, name='opening_hours'),
    path('opening_hours', views.add_opening_hours, name='add_opening_hours')
]
