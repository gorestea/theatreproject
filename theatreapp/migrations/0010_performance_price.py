# Generated by Django 4.2.1 on 2023-06-19 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatreapp', '0009_alter_hall_options_alter_ticket_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='price',
            field=models.IntegerField(default=300, verbose_name='Стоимость билета'),
        ),
    ]
