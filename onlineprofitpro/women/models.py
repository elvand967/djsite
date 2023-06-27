from django.db import models
from django.urls import reverse

class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")  # заголовок (тип — строковый, длина — 255 символов). Поле, обязательное к заполнению;
    content = models.TextField(blank=True, verbose_name="Текст статьи")  # сам текст (тип — memo) (blank=True - означает что поле может быть пустым);
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото") # параметр определяет в какой каталог будем загружать изображения
    # для корректной работы нужно настроить костанты
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания") # время создание новой записи (auto_now_add=True - после создания не изменяется)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения") # время обновления записи (auto_now=True - изменяется каждый раз после изменения)
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категория")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Известную женщину' # отображение в единственном числе
        verbose_name_plural = 'Известные женщины' # отображение в множественном числе
        ordering = ['-time_create', 'title'] # сортировка по обратной дате создания поста и названию
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    class Meta:
        verbose_name = 'Категорию' # отображение в единственном числе
        verbose_name_plural = 'Категории' # отображение в множественном числе
        ordering = ['id'] # сортировка по id

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})