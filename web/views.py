from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category,Products
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def homepage(request):
    return render(request,'homepage.html',)


def products(request):
    product = Products.objects.all()
    return render(request, 'products.html',{'product': product,})


def products_details(request,slug):
    product = Products.objects.filter(slug=slug)
    return render(request, 'products_detail.html',{'product': product,})



def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'user/login.html', {'form': form})



def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect('homepage')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def dashboard(request):

    return render(request, 'user/dashboard.html',)


def user_logout(request):
    logout(request)
    return redirect('homepage')


