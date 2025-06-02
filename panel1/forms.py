from django.forms import  *
from django import forms
from .models import *

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'email', 'role', 'status']
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_title', 'task_description', 'status', 'assigned_to']