# Generated by Django 4.1.7 on 2023-05-17 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_task_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='color',
            field=models.TextField(blank=True, max_length=7),
        ),
    ]