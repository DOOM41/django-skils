from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    text = models.TextField(verbose_name='Содержимое')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор'
    )
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Картинка')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата публикации'
    )
    reading_time = models.IntegerField(verbose_name='Время чтения ')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Cтатья'
        verbose_name_plural = 'Cтатьи'


class OtherImage(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name='Блог'
    )
    image = models.ImageField(
        "Фотография", null=True, upload_to="media/images"
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор')
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name='Блог')
    text = models.TextField(verbose_name='Коментарии')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата публикации')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарий'
