from datetime import datetime, date

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView, FormView
from .models import User, Profile
from .forms import UserForm, ProfileForm


def home(request):
    return render(request, "users/home.html")


def about(request):
    return render(request, 'users/about.html')


def user(request):
    hour_now = datetime.now().hour
    current_date = date.today()
    week_day = date.today().weekday()
    days = ["Понедельник", "Вторник", "Среда",
            "Четверг", "Пятница", "Суббота", "Воскресенье"]
    if hour_now < 12:
        greetings = "Доброе утро"
    elif hour_now < 18:
        greetings = "Добрый день"
    else:
        greetings = "Добрый вечер"
    data = {
        'title': greetings,
        'current_date': current_date,
        'week_day': days[week_day]
    }
    return render(request, 'main/index.html', data)


def profile(request):
    return render(request, 'users/profile.html')

class UserDetailView(DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'user_profile'


class ProfileDetailView(DetailView):
    model = Profile
    template_name = template_name = 'users/profile.html'
    context_object_name = 'user_profile_more'


class UpdateUser(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserForm


class UpdateProfile(UpdateView):
    model = Profile
    template_name = 'users/profile.html'
    form_class = ProfileForm


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
