from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import redirect, render
from .forms import LoginForm
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
                # print(user)
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
