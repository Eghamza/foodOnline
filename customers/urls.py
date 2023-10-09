from django.urls import path,include
from accounts import views as accountsView
from . import views


urlpatterns =[
      path('',accountsView.customerDashboard,name='customer'),
      path('cprofile/',views.cprofile, name='cprofile'),

]