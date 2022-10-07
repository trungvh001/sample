
from pydoc import classname
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from django.core.exceptions import ObjectDoesNotExist
from shool_app.models import CustomUser, Khoa, Lop, StudentManagement, Truong
from shool_app.util import check_class_create, check_class_edit, check_department_create, check_department_edit
from .forms import ClassForm, DepartmentForm, LoginForm, ShoolForm, StudentEditForm, StudentForm, UserCreateForm, UserEditForm
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


def list_shool(request):
    listshool = Truong.objects.all()
    context = {
        "user": request.user,
        'listshool': listshool}
    return render(request, 'listshool.html', context)


def add_new_shool(request):
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


def edit_shool(request, pk):
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


def add_new_department(request):
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            error_department, error_limit = check_department_create(form_data) 
            if error_limit:
                context = {
                    'typeform': 'Edit Department',
                    'form': form,
                    'error': 'Sức chứa của khoa k được vượt quá sức chứa của trường'
                }
                return render(request, 'form.html', context)
            elif error_department:
                context = {
                    'typeform': 'Add New Department',
                    'form': form,
                    'error': 'Khoa {department} đã tồn tại trong trường'.format(department=form_data['department'])
                }
                return render(request, 'form.html', context)
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
            form_data = form.cleaned_data
            error_department, error_limit = check_department_edit(form_data, pk) 
            if error_limit:
                context = {
                    'typeform': 'Edit Department',
                    'form': form,
                    'error': 'Sức chứa của khoa k được vượt quá sức chứa của trường'
                }
                return render(request, 'form.html', context)
            elif error_department:
                context = {
                    'typeform': 'Edit Department',
                    'form': form,
                    'error': 'Khoa đã tồn tại trong trường'
                }
                return render(request, 'form.html', context)
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


def add_new_class(request):
    form = ClassForm()
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            error_limit = check_class_create(form_data)
            if error_limit:
                context = {
                    'typeform': 'Add New Department',
                    'form': form,
                    'error': 'Sức chứa của lớp k được vượt quá sức chứa của khoa'
                }
                return render(request, 'form.html', context)
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
            form_data = form.cleaned_data
            error_limit = check_class_edit(form_data, pk)
            if error_limit:
                context = {
                    'typeform': 'Add New Department',
                    'form': form,
                    'error': 'Sức chứa của lớp k được vượt quá sức chứa của khoa'
                }
                return render(request, 'form.html', context)
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


def add_new_user(request):
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
    if pk == '1':
        return redirect('listuser')
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
    if pk == '1':
        return redirect('listuser')
    user = CustomUser.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('listuser')
    context = {
        'obj': user
    }
    return render(request, 'deleteconfirm.html', context)

def list_student(request):
    list_student = StudentManagement.objects.all()
    context = {
        'liststudent': list_student
    }
    return render(request, 'liststudent.html', context)


def add_student_to_class(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            student = CustomUser.objects.get(id=data['student'])
            classname = Lop.objects.get(id=data['classname'])
            try:
                check_exit = StudentManagement.objects.get(student=student)
            except ObjectDoesNotExist:
                check_exit = None
            if not check_exit:
                newstudent = StudentManagement(student=student, classname=classname)
                newstudent.save()
            else:
                context = {
                    'typeform': 'Add New Student in Class',
                    'form': form,
                    'error': 'Học sinh này đã có lớp, không thể thêm vào bất kì lớp nào khác'
                }
                return render(request, 'form.html', context)
        return redirect('liststudent')
    context = {
        'typeform': 'Add New Student in Class',
        'form': form
    }
    return render(request, 'form.html', context)

def edit_student_in_class(request, pk):
    studentclass = StudentManagement.objects.get(id=pk)
    form = StudentEditForm(initial={'classname': studentclass.classname.id})
    if request.method == 'POST':
        form = StudentEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            classname = Lop.objects.get(id=data['classname'])
            StudentManagement.objects.filter(id=pk).update(classname=classname)
        return redirect('liststudent')
    context = {
        'typeform': 'Edit student {namestudent} in Class'.format(namestudent=studentclass.student.username),
        'form': form
    }
    return render(request, 'form.html', context)