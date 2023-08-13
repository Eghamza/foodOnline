from django.contrib import admin
from .models import User,UserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name','role','is_active')
    filter_horizontal = ()
    list_filter=()
    ordering=('date_join',)
    fieldsets=()
admin.site.register(User,CustomUserAdmin)
admin.site.register(UserProfile)