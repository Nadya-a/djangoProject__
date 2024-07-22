from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
                  path('', views.home, name="home"),
                  path('signup/', views.SignUp.as_view(), name="signup"),
                  path('about/', views.about, name='about'),
                  path('completed/', views.completed, name='completed'),
                  path('user/', views.user, name='user'),
                  path('<int:pk>/profile/', views.UserDetailView.as_view(), name='profile'),
                  path('create', views.create, name='create'),
                  path('<int:pk>/update', views.TaskUpdateView.as_view(), name='task-update'),
                  path('<int:pk>/delete', views.TaskDeleteView.as_view(), name='task-delete')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
