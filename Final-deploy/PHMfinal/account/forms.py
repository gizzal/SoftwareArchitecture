from django import forms
from django.contrib.auth.models import User
from django.forms import PasswordInput, TextInput, EmailInput


class LoginForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'gui-input pl10',
               'placeholder': 'Input username...'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'gui-input pl10',
               'placeholder': 'Input password...'}))


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'gui-input pl10',
               'placeholder': 'Input password again...'}))

    class Meta:
        model = User
        fields = {"username", "email", "password"}
        widgets = {
            'password': PasswordInput(
                attrs={'class': 'gui-input pl10',
                       'placeholder': 'Input password...'}),
            'username': TextInput(
                attrs={'class': 'gui-input pl10',
                       'placeholder': 'Input username...'}),
            'email': EmailInput(
                attrs={'class': 'gui-input pl10',
                       'placeholder': 'Input email address...'}),
        }
