# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-11 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_constructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constructor',
            name='yeo_tag',
            field=models.CharField(max_length=100),
        ),
    ]