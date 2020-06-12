from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    # inja moshakhas mikonim che fieldhai bayad exzafe beshe
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User  # inja moshakhas mikonim classi k create kardim data ba che modeli ya tu kodum model zakhire beshe
        fields = ['username', 'email', 'password1', 'password2']
