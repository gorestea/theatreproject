# Generated by Django 4.2.1 on 2023-05-08 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Жанр')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название представления')),
                ('author', models.CharField(max_length=255, verbose_name='Автор')),
                ('time', models.CharField(max_length=255, verbose_name='Продолжительность')),
                ('date', models.DateTimeField(verbose_name='Продолжительность')),
                ('time_created', models.TimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('time_updated', models.TimeField(auto_now=True, verbose_name='Дата обновления')),
                ('about', models.TextField(blank=True, verbose_name='Описание')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Обложка')),
                ('is_published', models.BooleanField(default=True, verbose_name='Выгружено на сайт?')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='theatreapp.category', verbose_name='Категория')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='theatreapp.genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Представление',
                'verbose_name_plural': 'Представления',
                'ordering': ['-time_created'],
            },
        ),
    ]
