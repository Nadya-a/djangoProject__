# Generated by Django 4.1.7 on 2023-05-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_project_options_alter_task_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(verbose_name='Date: '),
        ),
    ]
