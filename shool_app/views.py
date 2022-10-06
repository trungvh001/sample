
from pydoc import classname
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from django.core.exceptions import ObjectDoesNotExist
from shool_app.models import CustomUser, Khoa, Lop, StudentClass, Truong
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
            form_data = form.cleaned_data
            if form_data['shool']:
                shool = Truong.objects.get(pk=form_data['shool'].id)
                error_limit = False
                error_department = False
                if shool.max_person < form_data['max_person']:
                    error_limit = True
                else:
                    list_department = Khoa.objects.filter(
                        shool=form_data['shool'])
                    count = 0
                    for dep_item in list_department:
                        if dep_item.department == form_data['department']:
                            error_department = True
                            break
                        count += dep_item.max_person
                    count += form_data['max_person']
                    if count > shool.max_person and error_department == False:
                        error_limit = True
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
            if form_data['shool']:
                shool = Truong.objects.get(pk=form_data['shool'].id)
                error_limit = False
                error_department = False
                if shool.max_person < form_data['max_person']:
                    error_limit = True
                else:
                    list_department = Khoa.objects.filter(
                        shool=form_data['shool'])
                    count = 0
                    for dep_item in list_department:
                        if dep_item.department == form_data['department']:
                            error_department = True
                            break
                        if dep_item.id == pk:
                            count += form_data['max_person']
                        else:
                            count += dep_item.max_person
                    if count > shool.max_person and error_department == False:
                        error_limit = True
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


def addnew_class(request):
    form = ClassForm()
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            if form_data['department']:
                department = Khoa.objects.get(pk=form_data['department'].id)
                error_limit = False
                if department.max_person < form_data['max_person']:
                    error_limit = True
                else:
                    list_class = Lop.objects.filter(
                        department=form_data['department'])
                    count = 0
                    for class_item in list_class:
                        count += class_item.max_person
                    count += form_data['max_person']
                    if count > department.max_person:
                        error_limit = True
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
            if form_data['department']:
                department = Khoa.objects.get(pk=form_data['department'].id)
                error_limit = False
                if department.max_person < form_data['max_person']:
                    error_limit = True
                else:
                    list_class = Lop.objects.filter(
                        department=form_data['department'])
                    count = 0
                    for class_item in list_class:
                        if class_item.id == pk:
                            count += form_data['max_person']
                        else:
                            count += class_item.max_person
                    if count > department.max_person:
                        error_limit = True
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
    list_student = StudentClass.objects.all()
    context = {
        'liststudent': list_student
    }
    return render(request, 'liststudent.html', context)


def addnew_studentclass(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            student = CustomUser.objects.get(id=data['student'])
            classname = Lop.objects.get(id=data['classname'])
            try:
                check_exit = StudentClass.objects.get(student=student)
            except ObjectDoesNotExist:
                check_exit = None
            if not check_exit:
                newstudent = StudentClass(student=student, classname=classname)
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

def edit_studentclass(request, pk):
    studentclass = StudentClass.objects.get(id=pk)
    form = StudentEditForm(initial={'classname': studentclass.classname.id})
    if request.method == 'POST':
        form = StudentEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            classname = Lop.objects.get(id=data['classname'])
            StudentClass.objects.filter(id=pk).update(classname=classname)
        return redirect('liststudent')
    context = {
        'typeform': 'Edit student {namestudent} in Class'.format(namestudent=studentclass.student.username),
        'form': form
    }
    return render(request, 'form.html', context)