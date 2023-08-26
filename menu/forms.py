
from django import forms
from menu.models import Categry


class add_category_forms(forms.ModelForm):
    class Meta:
        model = Categry

        fields = ['category_name','description']