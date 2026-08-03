from multiprocessing import context

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('You are logged in')
                else:
                    return HttpResponse('You are not active')
            else:
                return HttpResponse('Invalid login details')
    else:
        form = LoginForm()
        context = {'form': form}
    return render(request, 'registration/login.html', context=context)

def dashboard_view(request):
    user = request.user
    context = {
        'user': user
    }

    return render(request, 'pages/user_profile.html', context)

def user_register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            context = {'new_user': user_form}
            return render(request, 'account/register_done.html', context=context)
    else:
        user_form = RegisterForm()
        context = {'user_form': user_form}
        return render(request, 'account/register.html', context=context)