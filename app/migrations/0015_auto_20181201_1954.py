# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-01 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20181201_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='pages',
        ),
        migrations.AddField(
            model_name='app',
            name='pages',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Page'),
            preserve_default=False,
        ),
    ]