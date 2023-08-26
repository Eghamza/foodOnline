from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='vprofile'),
    path('menu_builder/', views.menu_builder, name='menu_builder'),
    path('food_item_category/<int:pk>',views.food_item_category, name='food_item_category'),

    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:pk>', views.edit_category, name='edit_category'),
]
