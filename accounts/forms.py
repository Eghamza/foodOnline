from typing import Any, Dict
from django import forms
from .models import User, UserProfile
from .validators import allow_only_image_validators


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    c_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'phone_number', 'password']
        
    def clean(self) -> Dict[str, Any]:
        data_cleaned = super(UserForm,self).clean()
        password = data_cleaned.get("password")     
        c_paswd = data_cleaned.get('c_password')

        if c_paswd != password:
            raise forms.ValidationError("conform password not match!")



class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'class':'btn btn-info'}), validators=[allow_only_image_validators]) #css
    cover_photo = forms.ImageField(widget=forms.FileInput(attrs={'class':'btn btn-info' }),validators=[allow_only_image_validators])
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'cover_photo', 'address_line_1','address_line_2','country','state','city','pin_code','latitude','longtitude']