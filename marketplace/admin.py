from django.contrib import admin
from .models import cart

# Register your models here.

class cartAdmin(admin.ModelAdmin):
    list_display = ('user','fooditem','quentity','created_at','updated_at',)

admin.site.register(cart,cartAdmin)