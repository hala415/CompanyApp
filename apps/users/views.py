from email import message
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
# Create your views here.

def home(request):
    return render(request, 'users/home.html')


def about(request):
    return render(request, 'users/about.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}')
            return redirect('users-home')
    else:
        form = UserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})

