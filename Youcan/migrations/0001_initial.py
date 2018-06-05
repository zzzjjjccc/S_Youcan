# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-24 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id_youcan', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('date', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('priority', models.IntegerField(default=0)),
                ('done', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Fans',
            fields=[
                ('id_youcan', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('fans', models.CharField(max_length=11, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Idols',
            fields=[
                ('id_youcan', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('idols', models.CharField(max_length=11, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Open',
            fields=[
                ('id_youcan', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('date', models.CharField(max_length=30)),
                ('open_to', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_youcan', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('school', models.CharField(max_length=80)),
                ('major', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('sex', models.CharField(max_length=5)),
            ],
        ),
    ]
