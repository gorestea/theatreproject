from django.db import models
from django.urls import reverse
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL


class Hall(models.Model):
    name = models.CharField(blank=True, max_length=80, unique=True)
    row = models.IntegerField(default=0)
    seat = models.IntegerField(default=0)

    objects = models.Model

    @property
    def total_seats(self):
        """calculating the number of seats in the hall"""
        total = self.row * self.seat
        return total

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        super(Hall, self).save(*args, **kwargs)

    def delete(self, using=None):
        self.is_deleted = True
        self.save()

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'
        ordering = ['name']


class Performance(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название представления')
    author = models.CharField(max_length=255, verbose_name='Автор')
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT, verbose_name='Жанр')
    time = models.CharField(max_length=255, verbose_name='Продолжительность')
    date = models.DateField(verbose_name='Дата представления')
    time_created = models.TimeField(verbose_name='Дата создания', auto_now_add=True)
    time_updated = models.TimeField(verbose_name='Дата обновления', auto_now=True)
    about = models.TextField(verbose_name='Описание', blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Обложка', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Выгружено на сайт?')
    hall = models.ForeignKey(Hall, null=True, on_delete=models.CASCADE, verbose_name='Зал')
    seats = models.IntegerField(default=0)
    price = models.IntegerField(default=300, verbose_name='Стоимость билета')

    objects = models.Model

    @property
    def seat_list(self):
        return [i for i in range(1, self.hall.seat + 1)]

    @property
    def row_list(self):
        return [i for i in range(1, self.hall.row + 1)]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Представление'
        verbose_name_plural = 'Представления'
        ordering = ['-time_created']

    def get_absolute_url(self):
        return reverse('performance', kwargs={'performance_slug': self.slug})


class Ticket(models.Model):
    email = models.EmailField(blank=True)
    seance = models.ForeignKey(Performance, null=True, on_delete=models.CASCADE)
    row = models.IntegerField(default=0)
    seat = models.IntegerField(default=0)

    objects = models.Model

    class Meta:
        """seats must be unique for one seance"""
        unique_together = ("seat", "row", "seance")

    def save(self, *args, **kwargs):
        super(Ticket, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.seance.name} {self.seance.date}"

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
        ordering = ['seance']


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    objects = models.Model

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})


class Genre(models.Model):
    name = models.CharField(max_length=255, verbose_name='Жанр')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    objects = models.Model

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('genre', kwargs={'genre_slug': self.slug})
