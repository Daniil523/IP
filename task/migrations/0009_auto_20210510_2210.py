# Generated by Django 3.2.2 on 2021-05-10 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_alter_time_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='task',
        ),
        migrations.AddField(
            model_name='item',
            name='time',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='task.time', verbose_name='Время'),
        ),
    ]