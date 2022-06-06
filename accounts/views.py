from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


def registerPage(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, 'User registered')
            return redirect('ngoDashboard')
        else:
            messages.error(request, 'Failed, Please Try Again.')

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('ngoDashboard')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Invalid User')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('ngoDashboard')
        else:
            messages.error(request, 'Invalid login credentials')
    context = {'page': page}

    return render(request, 'accounts/login.html', context)


def logoutpage(request):
    logout(request)
    messages.success(request, 'User logged out')
    return redirect('home')
