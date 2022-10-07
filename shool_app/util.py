
from shool_app.models import Khoa, Lop, Truong

def check_class_edit(form_data, pk):
    error_limit = False
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
    return error_limit


def check_class_create(form_data):
    error_limit = False
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
    return error_limit


def check_department_edit(form_data, pk):
    error_limit = False
    error_department = False
    if form_data['shool']:
        shool = Truong.objects.get(pk=form_data['shool'].id)
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
    return error_department, error_limit


def check_department_create(form_data, pk):
    error_limit = False
    error_department = False
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
    return error_department, error_limit
