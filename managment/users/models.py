from django.db import models
from django.contrib.auth.models import User
from django.db.models import ManyToManyField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Project(models.Model):
    name = models.TextField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Team(models.Model):
    short_name = models.TextField(max_length=50, blank=True)
    full_name = models.TextField(max_length=150, blank=True)
    project = ManyToManyField(Project)

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(max_length=4, blank=True)
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    job_title = models.TextField(max_length=200, blank=True)
    department = models.TextField(max_length=200, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='users/static/users/user_images', blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Task(models.Model):
    name = models.TextField(max_length=150, blank=True)
    description = models.TextField(max_length=500, blank=True)
    deadline = models.DateTimeField('Date: ')
    executor = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'