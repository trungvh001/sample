from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('listshool/', views.listshool, name='listshool'),
    path('addnewshool/', views.addnewshool, name='addnewshool'),
    path('editshool/<str:pk>', views.editshool, name='editshool'),
    path('deleteshool/<str:pk>', views.delete_shool, name='deleteshool'),
    path('listdepartment/', views.list_department, name='listdepartment'),
    path('addnewdepartment/', views.addnew_department, name='addnewdepartment'),
    path('editdepartment/<str:pk>', views.edit_department, name='editdepartment'),
    path('deletedepartment/<str:pk>', views.delete_department, name='deletedepartment'),
    path('listclass/', views.list_class, name='listclass'),
    path('addnewclass/', views.addnew_class, name='addnewclass'),
    path('editclass/<str:pk>', views.edit_class, name='editclass'),
    path('deleteclass/<str:pk>', views.delete_class, name='deleteclass'),
    path('listuser/', views.list_user, name='listuser'),
    path('addnewuser/', views.addnew_user, name='addnewuser'),
    path('edituser/<str:pk>', views.edit_user, name='edituser'),
    path('deleteuser/<str:pk>', views.delete_user, name='deleteuser'),
    path('liststudent/', views.list_student, name='liststudent'),
    path('addnewstudent/', views.addnew_studentclass, name='addnewstudent'),
    path('editstudent/<str:pk>', views.edit_studentclass, name='editstudent'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
