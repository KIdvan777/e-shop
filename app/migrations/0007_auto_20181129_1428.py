# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-29 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20181129_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='email',
            field=models.CharField(default=111, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='app',
            name='phone',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]