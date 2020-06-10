from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # inja moshakhas mikonim che fieldhai bayad exzafe beshe

    class Meta:
        model = User  # inja moshakhas mikonim classi k create kardim data ba che modeli ya tu kodum model zakhire beshe
        fields = ['username', 'email', 'password1', 'password2']
