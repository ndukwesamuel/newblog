from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
                    'username': forms.TextInput(attrs={'class': 'log_input', 'placeholder': 'username'}),
                    'email': forms.EmailInput(attrs={'class': 'log_input', 'placeholder': 'Email'}),
                    'password1':forms.PasswordInput (attrs={'class':'log_input', 'placeholder': 'password'}),
                    'password2':forms.PasswordInput(attrs={'class':'log_input', 'placeholder': 'password'  }),
                    
                }



