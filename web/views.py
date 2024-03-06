from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category,Products, Cart, CartItem
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.db import models
from django.shortcuts import render
from .utils import calculate_total_price


def homepage(request):
    product = Products.objects.all()
    return render(request,'pages/homepage.html',{'product': product,})


def products(request):
    product = Products.objects.all()
    return render(request, 'pages/products.html',{'product': product,})


def products_details(request,products_slug):
    product = get_object_or_404(Products, slug=products_slug)
    return render(request, 'pages/products_detail.html',{'product': product,})


def contact(request):
    return render(request,'pages/contact.html')



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

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    total_price = calculate_total_price(cart)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'pages/cart.html', {'cart_items': cart_items, 'total_price': total_price})



@login_required
def add_to_cart(request, products_slug):
    product = get_object_or_404(Products, slug=products_slug)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    quantity = int(request.POST.get('quantity', 1))

    if not item_created:
        cart_item.quantity += quantity
        cart_item.save()
    return redirect('view_cart')

@login_required
def remove_from_cart(request, products_slug):
    product = get_object_or_404(Products, slug=products_slug)
    cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.get(cart=cart, product=product)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('view_cart')