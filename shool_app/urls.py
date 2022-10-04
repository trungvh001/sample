from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('listshool/', views.listshool, name='listshool'),
    path('addnewshool/', views.addnewshool, name='addnewshool'),
    path('editshool/<str:pk>', views.editshool, name='editshool'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
