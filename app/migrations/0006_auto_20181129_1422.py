# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-29 14:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_slider_span'),
    ]

    operations = [
        migrations.RenameField(
            model_name='app',
            old_name='image',
            new_name='logo',
        ),
    ]