# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_project_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('basic', 'Basic'), ('Wordpress', (('generic_wordpress', 'Generic Wordpress'), ('sage', 'Sage Wordpress'))), ('django', 'Django'), ('rails', 'Ruby on Rails')], default='basic', max_length=1),
        ),
    ]