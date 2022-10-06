from django import forms
from django.forms import ModelForm
from .models import CustomUser, Truong, Khoa, Lop


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ShoolForm(ModelForm):
    class Meta:
        model = Truong
        fields = ['name', 'time_start', 'max_person', 'location']


class DepartmentForm(ModelForm):
    class Meta:
        model = Khoa
        fields = ['name', 'department', 'max_person', 'shool']


class ClassForm(ModelForm):
    class Meta:
        model = Lop
        fields = ['name', 'max_person', 'department']


class UserCreateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'full_name',
                  'role', 'date_of_birth', 'location', 'is_active']


class UserEditForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'full_name', 'role',
                  'date_of_birth', 'location', 'is_active']


class StudentForm(forms.Form):
    student = forms.ChoiceField(choices=[
    (choice.pk, choice) for choice in CustomUser.objects.filter(role='01')],required=True)
    classname = forms.ChoiceField(choices=[
    (choice.pk, choice) for choice in Lop.objects.all()],required=True)

class StudentEditForm(forms.Form):
    classname = forms.ChoiceField(choices=[
    (choice.pk, choice) for choice in Lop.objects.all()],required=True)