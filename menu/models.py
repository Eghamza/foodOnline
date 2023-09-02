from django.db import models
from vendor.models import Vendor 

# Create your models here.

class Categry(models.Model):
    vendor = models.ForeignKey(Vendor, models.CASCADE, blank=True)
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100)
    description = models.TextField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def clean(self):
        self.category_name = self.category_name.capitalize()

    def __str__(self):
        return self.category_name
    


class FoodItem(models.Model):
    vendor = models.ForeignKey(Vendor, models.CASCADE)
    categry = models.ForeignKey(Categry,models.CASCADE,related_name='fooditems')
    food_title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique= True)
    discription = models.TextField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='foodimages')


    def __str__(self):
        return self.food_title


