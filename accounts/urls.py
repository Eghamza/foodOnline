from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.myAccount),
    path('register/', views.register, name='register'),
    path('registervendor/', views.registervendor, name='registervendor'),

    #login 
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('myaccount/', views.myAccount, name='myaccount'),
    #path('customerDashboard/', views.customerDashboard, name='customerDashboard'),
    path('vendorDashboard/', views.vendorDashboard, name='vendorDashboard'),
    path('dashbourd/', views.dashbourd, name='dashbourd'),


    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    
#foget password verification
    path('forget_password/', views.forget_password, name='forget_password'),
    path('reset_password_verify/<uidb64>/<token>/',views.reset_password_validate,name='reset_password_validate'),
    path('reset_password/',views.reset_password,name='reset_password'),
    
    path('vendor/', include('vendor.urls')),
    path('customer/', include('customers.urls')),

]
