# Generated by Django 4.2.1 on 2023-05-23 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatreapp', '0005_remove_hall_created_at_remove_ticket_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='date',
            field=models.DateField(verbose_name='Дата представления'),
        ),
    ]
