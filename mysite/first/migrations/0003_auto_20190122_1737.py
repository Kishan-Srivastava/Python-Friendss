# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-01-22 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_auto_20190122_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.FileField(null=True, upload_to='media/images/', verbose_name=''),
        ),
    ]