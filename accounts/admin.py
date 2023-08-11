from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
   list_display = ('email', 'username', 'first_name', 'last_name')
    # filter_horizontal = ()
    # filter_list = ()
    # fieldsets=()
admin.site.register(User, CustomUserAdmin)
