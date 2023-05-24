from datetime import datetime, date, timedelta
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView, FormView, DeleteView
from .models import User, Task, Project, Team
from .forms import TaskForm


def home(request):
    return render(request, "users/home.html")


def about(request):
    current_date = date.today()
    tomorrow = current_date + timedelta(1)
    yesterday = current_date - timedelta(1)
    tasks = Task.objects.filter(status='incomplete').order_by('deadline')
    projects = Project.objects.order_by('id')
    teams = Team.objects.order_by('id')

    data = {
        'tasks': tasks,
        'projects': projects,
        'teams': teams,
        'current_date': current_date,
        'tomorrow': tomorrow,
        'yesterday': yesterday
    }

    return render(request, 'users/about.html', data)

def completed(request):
    current_date = date.today()
    tomorrow = current_date + timedelta(1)
    yesterday = current_date - timedelta(1)
    tasks = Task.objects.filter(status='completed').order_by('deadline')
    projects = Project.objects.order_by('id')
    teams = Team.objects.order_by('id')

    data = {
        'tasks': tasks,
        'projects': projects,
        'teams': teams,
        'current_date': current_date,
        'tomorrow': tomorrow,
        'yesterday': yesterday
    }

    return render(request, 'users/about.html', data)

def user(request):
    hour_now = datetime.now().hour
    current_date = date.today()
    tomorrow = current_date + timedelta(1)
    yesterday = current_date - timedelta(1)
    week_day = date.today().weekday()
    days = ["Понедельник", "Вторник", "Среда",
            "Четверг", "Пятница", "Суббота", "Воскресенье"]
    if hour_now < 12:
        greetings = "Доброе утро"
    elif hour_now < 18:
        greetings = "Добрый день"
    else:
        greetings = "Добрый вечер"

    tasks = Task.objects.order_by('deadline')
    projects = Project.objects.order_by('id')
    teams = Team.objects.order_by('id')

    data = {
        'title': greetings,
        'week_day': days[week_day],
        'username': request.user.username,
        'tasks': tasks,
        'projects': projects,
        'teams': teams,
        'current_date': current_date,
        'tomorrow': tomorrow,
        'yesterday': yesterday
    }

    return render(request, 'main/index.html', data)


def profile(request):
    return render(request, 'users/profile.html')


class UserDetailView(DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'user_profile'


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def create(request):
    text = 'Создание задачи'
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
        else:
            error = 'Invalid forma'

    form = TaskForm()

    data = {
        'form': form,
        'error': error,
        'text': text
    }

    return render(request, 'users/task_update.html', data)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'users/task_update.html'
    form_class = TaskForm


class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/about/'
    template_name = 'users/task_delete.html'
