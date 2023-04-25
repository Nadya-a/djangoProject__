# Generated by Django 4.1.7 on 2023-04-12 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nazvanie')),
                ('anons', models.CharField(max_length=150, verbose_name='Anons')),
                ('full_text', models.TextField(verbose_name='Full text')),
                ('date', models.DateTimeField(verbose_name='Date: ')),
            ],
        ),
    ]
