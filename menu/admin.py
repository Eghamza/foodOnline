from django.contrib import admin
from .models import Categry,FoodItem

# Register your models here.
class CategryAdmin(admin.ModelAdmin):
   prepopulated_fields = {'slug':('category_name',)}
   list_display = ('category_name','vendor')


class FoodItemAdmin(admin.ModelAdmin):
   prepopulated_fields = {'slug':('food_title',)}  
   list_display = ('food_title','categry','vendor','price','is_available')
admin.site.register(Categry,CategryAdmin)
admin.site.register(FoodItem,FoodItemAdmin)