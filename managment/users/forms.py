from .models import User, Profile
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, ImageField


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'email'
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'first name'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'last name'
            })
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['department', 'bio', 'photo']

        widgets = {
            'department': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'department'
            }),
            'bio': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'bio'
            }),
            'photo': ImageField()
        }
