# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runze', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='empresa/')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=400)),
            ],
        ),
    ]