# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 22:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ta_logistics_application', '0011_status_class_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Status',
        ),
    ]
