# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 07:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default=None, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('taille', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('prix', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='pizza',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Pizza'),
        ),
    ]