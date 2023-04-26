from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


def home(request):
    return render(request, "users/home.html")


def about(request):
    return render(request, 'main/about.html')

def user(request):
    return render(request, 'main/index.html')

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"