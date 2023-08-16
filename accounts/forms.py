from typing import Any, Dict
from django import forms
from .models import User


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
