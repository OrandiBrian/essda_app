from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreationView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserChangeForm, RegistrationForm
from .models import CustomUser
from .decorators import role_required

# user login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not none:
            login(request, user)
            message.success(request, "You have successfully logged in!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")
            
    return render(request, 'accounts/login.html')

# user logout
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('login')

#