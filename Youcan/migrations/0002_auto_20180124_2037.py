# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-24 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Youcan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='phone',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='fans',
            name='phone',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='idols',
            name='phone',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='open',
            name='phone',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
