from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, null=True, verbose_name="Категория")
    status = models.ForeignKey('Status', on_delete=models.DO_NOTHING, null=True, verbose_name="Статус")
    time = models.OneToOneField("Time", on_delete=models.DO_NOTHING, null=True, verbose_name="Время")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Status(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Label(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    color = models.CharField(max_length=150, verbose_name="Цвет")
    item = models.ForeignKey('Item', on_delete=models.DO_NOTHING, null=True, verbose_name="Задача")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ярлык'
        verbose_name_plural = 'Ярлыки'


class Project(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    people = models.ManyToManyField(User, verbose_name="Люди")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Time(models.Model):
    start = models.TimeField(verbose_name="Начало")
    endPoint = models.TimeField(null=True, verbose_name="Планируемое окончание")
    endFact = models.TimeField(null=True, verbose_name="Фактическое окончание")

    class Meta:
        verbose_name = 'Время'
        verbose_name_plural = 'Времена'
