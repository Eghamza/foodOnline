from django import forms
from .models import Vendor


class vendonForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['vendor_name', 'vendor_licence']
