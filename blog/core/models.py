from tabnanny import verbose
from unicodedata import category
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length = 255, verbose_name = 'Категория')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Post(models.Model):
    categoryies = models.ManyToManyField(Category, related_name = 'category')
    topic = models.CharField(max_length = 255, verbose_name = 'Тема')
    text = models.TextField(verbose_name = 'Пост')
    date = models.DateTimeField(verbose_name='Время создания')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('topic','date')


class User(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'post')
    first_name = models.CharField(max_lenght = 255, verbose_name='Имя')
    last_name = models.CharField(max_lenght = 255, verbose_name='Фамилия')
    gender = models.CharField(max_lenght = 255, verbose_name='Пол')
    email = models.EmailField(verbose_name = 'Электронная почта')
    about = models.TextField(verbose_name='О себе')
    photo = models.ImageField(verbose_name='Фото')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('first_name', 'last_name')