from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Kullanıcı Adı',
            'email': 'E-posta',
            'password1': 'Şifre',
            'password2': 'Şifre Tekrar',
        }

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')
        labels = {
            'username': 'Kullanıcı Adı',
            'password': 'Şifre',
        }


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Kullanıcı Adı',
            'email': 'E-posta',
            'password': 'Şifre'
        }


