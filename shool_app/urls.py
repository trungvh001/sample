from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('listshool/', views.list_shool, name='listshool'),
    path('addnewshool/', views.add_new_shool, name='addnewshool'),
    path('editshool/<str:pk>', views.edit_shool, name='editshool'),
    path('deleteshool/<str:pk>', views.delete_shool, name='deleteshool'),
    path('listdepartment/', views.list_department, name='listdepartment'),
    path('addnewdepartment/', views.add_new_department, name='addnewdepartment'),
    path('editdepartment/<str:pk>', views.edit_department, name='editdepartment'),
    path('deletedepartment/<str:pk>', views.delete_department, name='deletedepartment'),
    path('listclass/', views.list_class, name='listclass'),
    path('addnewclass/', views.add_new_class, name='addnewclass'),
    path('editclass/<str:pk>', views.edit_class, name='editclass'),
    path('deleteclass/<str:pk>', views.delete_class, name='deleteclass'),
    path('listuser/', views.list_user, name='listuser'),
    path('addnewuser/', views.add_new_user, name='addnewuser'),
    path('edituser/<str:pk>', views.edit_user, name='edituser'),
    path('deleteuser/<str:pk>', views.delete_user, name='deleteuser'),
    path('liststudent/', views.list_student, name='liststudent'),
    path('addnewstudent/', views.add_student_to_class, name='addnewstudent'),
    path('editstudent/<str:pk>', views.edit_student_in_class, name='editstudent'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
