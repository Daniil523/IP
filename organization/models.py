from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    people = models.ManyToManyField(User, verbose_name="Люди")
    projects = models.ForeignKey('task.Project', verbose_name="Проекты", on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class Attainments(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'


class Points(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    team = models.ManyToManyField(User, verbose_name="Команда")

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'

