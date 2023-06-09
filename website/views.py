from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def home(request):
    # check for if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have login successful!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Login, Please Try Again")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have logout ...")
    return redirect('home')

