# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-01-22 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0006_auto_20190122_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
