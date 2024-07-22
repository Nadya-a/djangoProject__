from datetime import date, timedelta

from .models import User, Profile, Task, Project
from django.forms import ModelForm, TextInput, Textarea, ImageField, ModelChoiceField, DateInput, ChoiceField


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



TASK_STATUSES = (
        ('completed', 'COMPLETED'),
        ('incomplete', 'incomplete')
    )
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'deadline', 'executor', 'project', 'status']
        executor = ModelChoiceField(queryset=Profile.objects.all(), to_field_name="user")
        executor.widget.attrs.update({'class': 'form-control'})
        project = ModelChoiceField(queryset=Project.objects.all(), to_field_name="name")
        project.widget.attrs.update({'class': 'form-control'})
        status = ChoiceField(choices=TASK_STATUSES)
        current_date = date.today() + timedelta(1)

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control'
            }),
            'description': Textarea(attrs={
                'class': 'form-control'
            }),
            'deadline': DateInput(attrs={
                'class': 'form-control',
                'value': current_date
            })
        }
