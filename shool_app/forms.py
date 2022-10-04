from django import forms
from django.forms import ModelForm
from .models import Truong

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class AddNewShoolForm(ModelForm):
    class Meta:
        model = Truong
        fields = ['name', 'time_start', 'max_person', 'location']