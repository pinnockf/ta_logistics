# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-17 06:44
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('ta_logistics_application', '0004_auto_20161017_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='selected_optional_field_ids',
            field=models.CharField(max_length=40, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')]),
        ),
        migrations.AlterField(
            model_name='applicationstatus',
            name='date_submitted',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='teaching_experience',
            field=models.CharField(default='', max_length=400),
        ),
    ]