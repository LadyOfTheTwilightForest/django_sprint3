from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
    

class BaseModel(models.Model):
    is_published = models.BooleanField(
        default=True, blank=True, verbose_name = 'Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
        )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name = 'Добавлено')

    class Meta:
        abstract = True

class Category(BaseModel):
    title = models.CharField(max_length = 256, blank=True, verbose_name = 'Заголовок')
    description  = models.TextField(blank=True, verbose_name = 'Описание')
    slug = models.SlugField(
        unique=True, blank = True, verbose_name = 'Идентификатор',
        help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.'
        )
    # empty_value_display = ''
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

class Location(BaseModel):
    name = models.CharField(max_length = 256, blank=True, verbose_name = 'Название места')
    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Post(BaseModel):
    title = models.CharField(max_length = 256, blank=True, verbose_name = 'Заголовок')
    text  = models.TextField(blank=True, verbose_name = 'Текст')
    pub_date = models.DateTimeField(
        blank=True, verbose_name = 'Дата и время публикации',
        help_text='Если установить дату и время в будущем — можно делать отложенные публикации.'
        )
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name = 'Автор публикации')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=False, verbose_name = 'Местоположение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False, verbose_name = 'Категория')

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title

