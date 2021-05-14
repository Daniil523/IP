# Generated by Django 3.2.2 on 2021-05-10 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0009_auto_20210510_2210'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='projects',
        ),
        migrations.AddField(
            model_name='organization',
            name='projects',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='task.project', verbose_name='Проекты'),
        ),
    ]