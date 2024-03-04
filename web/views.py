from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category,Products, Cart, CartItem
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def homepage(request):
    return render(request,'homepage.html',)


def products(request):
    product = Products.objects.all()
    return render(request, 'products.html',{'product': product,})


def products_details(request,products_slug):
    product = get_object_or_404(Products, slug=products_slug)
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

@login_required
def view_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.items.all()
        return render(request, 'cart.html', {'cart_items': cart_items,})
    else:
        redirect('homepage')
    return render(request, 'cart.html', {'cart': user_cart})



def add_to_cart(request, products_slug):
    product = get_object_or_404(Products, slug=products_slug)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return render(request, 'cart.html', {'cart': cart})

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

    return render(request, 'cart.html', {'cart': cart})

