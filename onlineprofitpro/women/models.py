from django.db import models
from django.urls import reverse

class Women(models.Model):
    title = models.CharField(max_length=255)  # заголовок (тип — строковый, длина — 255 символов). Поле, обязательное к заполнению;
    content = models.TextField(blank=True)  # сам текст (тип — memo) (blank=True - означает что поле может быть пустым);
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/") # параметр определяет в какой каталог будем загружать изображения
    # для корректной работы нужно настроить костанты
    time_create = models.DateTimeField(auto_now_add=True) # время создание новой записи (auto_now_add=True - после создания не изменяется)
    time_update = models.DateTimeField(auto_now=True) # время обновления записи (auto_now=True - изменяется каждый раз после изменения)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})