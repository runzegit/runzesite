# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runze', '0005_conteudo_ordem'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='descricao',
            field=models.CharField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, error amet numquam iure provident voluptate esse quasi, veritatis totam voluptas nostrum quisquam eum porro a pariatur accusamus veniam. Quia, minima', max_length=400),
            preserve_default=False,
        ),
    ]