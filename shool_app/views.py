import email
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import redirect, render
from django.urls import is_valid_path

from shool_app.models import CustomUser, Khoa, Lop, Truong
from .forms import ClassForm, DepartmentForm, LoginForm, ShoolForm, UserCreateForm, UserEditForm
# Create your views here.

def home(request):
    context = {}
    if request.user.is_authenticated:
        context = {
            "user": request.user
        }
    return render(request, 'index.html', context)


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_data = login_form.cleaned_data
            user = authenticate(request,
                                username=login_data['username'],
                                password=login_data['password'])
            if user is not None:
                auth_login(request, user)
                return redirect('/home')
    else:
        login_form = LoginForm()
    context = {
        "login_form": login_form,
    }

    return render(request, 'login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('/login')


def listshool(request):
    listshool = Truong.objects.all()
    context = {
        "user": request.user,
        'listshool': listshool}
    return render(request, 'listshool.html', context)


def addnewshool(request):
    form = ShoolForm()
    if request.method == 'POST':
        form = ShoolForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listshool')
    context = {
        'typeform': 'Add New Shool',
        'form': form
    }
    return render(request, 'form.html', context)


def editshool(request, pk):
    shool = Truong.objects.get(id=pk)
    form = ShoolForm(instance=shool)
    if request.method == 'POST':
        form = ShoolForm(request.POST, instance=shool)
        if form.is_valid():
            form.save()
        return redirect('listshool')
    context = {
        'typeform': 'Edit Shool',
        'form': form
    }
    return render(request, 'form.html', context)


def delete_shool(request, pk):
    shool = Truong.objects.get(id=pk)
    if request.method == 'POST':
        shool.delete()
        return redirect('listshool')
    context = {
        'obj': shool
    }
    return render(request, 'deleteconfirm.html', context)

def list_department(request):
    listdepartment = Khoa.objects.all()
    context = {
        "user": request.user,
        'listdepartment': listdepartment}
    return render(request, 'listdepartment.html', context)


def addnew_department(request):
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listdepartment')
    context = {
        'typeform': 'Add New Department',
        'form': form
    }
    return render(request, 'form.html', context)


def edit_department(request, pk):
    department = Khoa.objects.get(id=pk)
    form = DepartmentForm(instance=department)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
        return redirect('listdepartment')
    context = {
        'typeform': 'Edit Department',
        'form': form
    }
    return render(request, 'form.html', context)

def delete_department(request, pk):
    department = Khoa.objects.get(id=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('listdepartment')
    context = {
        'obj': department
    }
    return render(request, 'deleteconfirm.html', context)

def list_class(request):
    listclass = Lop.objects.all()
    context = {
        "user": request.user,
        'listclass': listclass}
    return render(request, 'listclass.html', context)


def addnew_class(request):
    form = ClassForm()
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listclass')
    context = {
        'typeform': 'Add New Class',
        'form': form
    }
    return render(request, 'form.html', context)


def edit_class(request, pk):
    classInstance = Lop.objects.get(id=pk)
    form = ClassForm(instance=classInstance)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=classInstance)
        if form.is_valid():
            form.save()
        return redirect('listclass')
    context = {
        'typeform': 'Edit Class',
        'form': form
    }
    return render(request, 'form.html', context)

def delete_class(request, pk):
    classInstance = Lop.objects.get(id=pk)
    if request.method == 'POST':
        classInstance.delete()
        return redirect('listclass')
    context = {
        'obj': classInstance
    }
    return render(request, 'deleteconfirm.html', context)

def list_user(request):
    listuser = CustomUser.objects.all()
    context = {
        "user": request.user,
        'listuser': listuser
    }
    return render(request, 'listuser.html', context)


def addnew_user(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data["username"]
            password = data["password"]
            item = {
                "email": data["email"],
                "full_name": data["full_name"],
                "role": data["role"],
                "is_active": data["is_active"],
                "date_of_birth": data["date_of_birth"],
                "location": data["location"],
            }
            CustomUser.objects.create_user(
                username, password, **item)
        return redirect('listuser')
    context = {
        'typeform': 'Add New User',
        'form': form
    }
    return render(request, 'form.html', context)


def edit_user(request, pk):
    user = CustomUser.objects.get(id=pk)
    form = UserEditForm(instance=user)
    if request.method == 'POST':

        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('listuser')
    context = {
        'typeform': 'Edit User',
        'form': form
    }
    return render(request, 'form.html', context)

def delete_user(request, pk):
    user = CustomUser.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('listuser')
    context = {
        'obj': user
    }
    return render(request, 'deleteconfirm.html', context)