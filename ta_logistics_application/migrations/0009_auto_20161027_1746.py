# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-27 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ta_logistics_application', '0008_classes_is_active'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StatusText',
        ),
        migrations.AlterField(
            model_name='classapplicants',
            name='application_status_id',
            field=models.IntegerField(choices=[(0, 'Application Submitted'), (1, 'Application Pending'), (2, 'Application Complete')], default=0),
        ),
        migrations.AlterField(
            model_name='classapplicants',
            name='hiring_status_id',
            field=models.IntegerField(choices=[(0, 'Pending Review'), (1, 'Rejected'), (2, 'Interviewing'), (3, 'Accepted'), (4, 'Wait Listed')], default=0),
        ),
    ]