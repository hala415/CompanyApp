from email import message
from msilib.schema import ListView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from .forms import UserRegisterForm
from .filter import UserFilter
# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def about(request):
    return render(request, 'users/about.html')

def style_base(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'users/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}')
            return redirect('users-home')
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})


class UserListView(ListView):
    model = UserCreationForm
    

