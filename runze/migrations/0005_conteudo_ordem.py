# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runze', '0004_auto_20170711_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='conteudo',
            name='ordem',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
