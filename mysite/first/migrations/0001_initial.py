# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-10 11:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('birthday', models.DateField(default=datetime.date.today)),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('desc', models.TextField(blank=True, max_length=100)),
                ('photo', models.FileField(blank=True, upload_to='')),
            ],
        ),
    ]
