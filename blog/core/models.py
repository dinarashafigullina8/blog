from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length = 255, verbose_name = 'Категория')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class User(models.Model):
    man = 'М'
    women = 'Ж'
    gender_choices = [
        (man, 'Мужчина'),
        (women, 'Женщина')
    ]
    first_name = models.CharField(max_length = 255, verbose_name='Имя')
    last_name = models.CharField(max_length = 255, verbose_name='Фамилия')
    gender = models.CharField(max_length = 255, choices = gender_choices, verbose_name='Пол')
    email = models.EmailField(verbose_name = 'Электронная почта')
    about = models.TextField(verbose_name='О себе')
    photo = models.ImageField(default='-', verbose_name='Фото')

    # def __str__(self):
    #     return self.name
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('first_name', 'last_name')


class Post(models.Model):
    categoryies = models.ManyToManyField(Category, related_name = 'category')
    author = models.ForeignKey(User, on_delete = models.CASCADE,related_name = 'user', default=0)
    topic = models.CharField(max_length = 255, verbose_name = 'Тема')
    text = models.TextField(verbose_name = 'Пост')
    image = models.ImageField(upload_to="images/", default='-', verbose_name='Фото')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    # def __str__(self):
    #     return self.name
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('topic','date')