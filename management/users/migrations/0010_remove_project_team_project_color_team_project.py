# Generated by Django 4.1.7 on 2023-05-26 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_project_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='team',
        ),
        migrations.AddField(
            model_name='project',
            name='color',
            field=models.TextField(blank=True, max_length=7),
        ),
        migrations.AddField(
            model_name='team',
            name='project',
            field=models.ManyToManyField(to='users.project'),
        ),
    ]
