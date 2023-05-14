from django.contrib.auth.models import User
from django.shortcuts import render
from datetime import datetime

from django.views.generic import DetailView


# Create your views here.
def index(request):
    hour_now = datetime.now().hour
    if hour_now < 12:
        greetings = "Доброе утро"
    elif hour_now < 18:
        greetings = "Добрый день"
    else:
        greetings = "Добрый вечер"
    data = {
        'title': greetings
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'users/about.html')


def profile(request):
    return render(request, 'users/profile.html')


class UserDetailView(DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'user_profile'

