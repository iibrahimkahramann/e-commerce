from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('contact/', views.contact, name='contact'),
    path('logout/', views.user_logout, name='user_logout'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('products/', views.products, name='products'),
    path('products/<slug:products_slug>', views.products_details, name='products_detail'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add_to_cart/<slug:products_slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug:product_slug>/', views.remove_from_cart, name='remove_from_cart'),


]
