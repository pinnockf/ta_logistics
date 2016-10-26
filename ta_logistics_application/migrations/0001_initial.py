# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-15 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=30)),
                ('is_default', models.BooleanField()),
                ('data_type', models.CharField(max_length=6)),
                ('max_length', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('class_id', models.IntegerField()),
                ('application_status_id', models.IntegerField()),
                ('hiring_status_id', models.IntegerField()),
                ('date_submitted', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor_id', models.IntegerField()),
                ('active_semester', models.CharField(max_length=4)),
                ('class_listing_id', models.CharField(max_length=6)),
                ('class_name', models.CharField(max_length=20)),
                ('available_hours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Professors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubit_name', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='StatusText',
            fields=[
                ('status_type', models.IntegerField(primary_key=True, serialize=False)),
                ('status_id', models.IntegerField()),
                ('status_text', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubit_name', models.CharField(max_length=10)),
                ('person_number', models.CharField(max_length=8)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gpa', models.FloatField()),
                ('resume', models.FileField(upload_to='resumes/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('teaching_experience', models.CharField(max_length=140)),
            ],
        ),
    ]
