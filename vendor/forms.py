from django import forms
from .models import Vendor, OpeningHours
from accounts.validators import allow_only_image_validators


class vendonForm(forms.ModelForm):
    vendor_licence = forms.FileField(widget= forms.FileInput(attrs={'class': 'btn btn-info'}),validators=[allow_only_image_validators])
    class Meta:
        model = Vendor
        fields = ['vendor_name', 'vendor_licence']


class openingForm(forms.ModelForm):

    class Meta:
        model = OpeningHours
        fields = ['day','from_hour','to_hour','is_closed']


