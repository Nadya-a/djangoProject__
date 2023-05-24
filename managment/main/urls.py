from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/profile/', views.UserDetailView.as_view(), name='profile')
]