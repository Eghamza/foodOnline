
from django import forms
from menu.models import Categry, FoodItem
from accounts.validators import allow_only_image_validators


class add_category_forms(forms.ModelForm):
    class Meta:
        model = Categry

        fields = ['category_name','description']


class food_item_forms(forms.ModelForm):
            image = forms.FileField(widget= forms.FileInput(attrs={'class': 'btn btn-info'}),validators=[allow_only_image_validators])
            class Meta:
                model = FoodItem

                fields = ['food_title','categry','price','discription','image']
                   