from django import forms
from .models import Todo
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class NewTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description')
        widgets = {
            'title' : forms.TextInput(attrs={
                'class': 'ml-2 py-2 px-6 rounded-xl border w-1/3 flex'
            }),
            'description': forms.Textarea(attrs={
                'class': 'ml-2 py-4 px-6 rounded-xl border w-1/2 flex'
            }),
        }


class EditTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'complete')
        widgets = {
            'title' : forms.TextInput(attrs={
                'class': 'py-4 px-6 rounded-xl border w-full'
            }),
            'description': forms.Textarea(attrs={
                'class': 'py-4 px-6 rounded-xl border w-full'
            }),
            'complete': forms.CheckboxInput(attrs={
                'class': 'py-4 px-6 rounded-xl border w-full'
            }),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter username',
        'class': 'w-full py-2 px-4 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password',
        'class': 'w-full py-2 px-4 rounded-xl'
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter username',
        'class': 'w-full py-2 px-4 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter email address',
        'class': 'w-full py-2 px-4 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password',
        'class': 'w-full py-2 px-4 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-2 px-4 rounded-xl'
    }))

