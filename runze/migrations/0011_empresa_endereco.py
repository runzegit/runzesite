# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runze', '0010_contato_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='endereco',
            field=models.CharField(default='Rua Cel. Manoel Bandeira, 1227 - Centro - Imperatriz-MA | CEP 659000-010', max_length=400),
            preserve_default=False,
        ),
    ]
