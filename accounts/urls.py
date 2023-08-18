from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('registervendor/', views.registervendor, name='registervendor'),

    #login 
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('myaccount/', views.myAccount, name='myaccount'),
    path('customerDashboard/', views.customerDashboard, name='customerDashboard'),
    path('vendorDashboard/', views.vendorDashboard, name='vendorDashboard'),
    path('dashbourd/', views.dashbourd, name='dashbourd'),
    path('activate/<uidb64>/<token>',views.activate, name='activate'),
    
]
