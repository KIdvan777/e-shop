# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-30 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20181130_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='social_links',
        ),
        migrations.AddField(
            model_name='app',
            name='social_links',
            field=models.ManyToManyField(to='app.Social'),
        ),
    ]
