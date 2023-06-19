# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SuccessNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('InvId', models.IntegerField(verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0437\u0430\u043a\u0430\u0437\u0430', db_index=True)),
                ('OutSum', models.CharField(max_length=15, verbose_name='\u0421\u0443\u043c\u043c\u0430')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0423\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0435 \u043e\u0431 \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u043c \u043f\u043b\u0430\u0442\u0435\u0436\u0435',
                'verbose_name_plural': '\u0423\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f \u043e\u0431 \u0443\u0441\u043f\u0435\u0448\u043d\u044b\u0445 \u043f\u043b\u0430\u0442\u0435\u0436\u0430\u0445 (ROBOKASSA)',
            },
            bases=(models.Model,),
        ),
    ]
