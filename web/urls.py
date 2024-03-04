from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('logout/', views.user_logout, name='user_logout'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('ürünler/', views.products, name='products'),
    path('ürünler/<slug:products_slug>', views.products_details, name='products_detail'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add_to_cart/<slug:products_slug>/', views.add_to_cart, name='add_to_cart'),


]
