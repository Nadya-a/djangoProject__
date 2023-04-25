from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), # до регистр/автор было home path('', views.index, name='index')
    path('about', views.about, name='about')
]