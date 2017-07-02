# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170702_0958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='pizza',
            name='ingredients',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='app.Ingredient'),
        ),
    ]
