# Generated by Django 3.2.2 on 2021-05-10 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_time_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='task.item', verbose_name='Задача'),
        ),
    ]
