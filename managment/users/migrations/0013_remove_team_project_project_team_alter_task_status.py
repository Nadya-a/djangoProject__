# Generated by Django 4.1.7 on 2023-06-28 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.team'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('completed', 'COMPLETED'), ('incomplete', 'INCOMPLETE')], default='incomplete', max_length=10),
        ),
    ]