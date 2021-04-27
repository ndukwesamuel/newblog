from django import forms
from django.forms import ModelForm

from home.models import Forum

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class post_form(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['author', 'title', 'message']


class cry_form(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['author', 'title', 'message']


