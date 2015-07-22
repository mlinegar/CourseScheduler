# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('term_code', models.CharField(max_length=6)),
                ('CRN', models.CharField(max_length=5)),
                ('note', models.CharField(max_length=250, default='')),
                ('course', models.CharField(max_length=12, default='')),
                ('title', models.CharField(max_length=50, default='')),
                ('xlist', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=12), size=None)),
                ('instructor', models.CharField(max_length=122, default='')),
                ('group', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1), size=None)),
                ('graduate_level', models.BooleanField(default=False)),
                ('year_long', models.BooleanField(default=False)),
                ('subject', models.CharField(max_length=30, default='')),
                ('status', models.CharField(max_length=9, default='')),
                ('units', models.DecimalField(max_digits=3, decimal_places=1)),
                ('add_me', models.CharField(max_length=200, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Courses_location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('day_number', models.CharField(max_length=1)),
                ('SUN_day', models.BooleanField(default=False)),
                ('MON_day', models.BooleanField(default=False)),
                ('TUE_day', models.BooleanField(default=False)),
                ('WED_day', models.BooleanField(default=False)),
                ('THU_day', models.BooleanField(default=False)),
                ('FRI_day', models.BooleanField(default=False)),
                ('SAT_day', models.BooleanField(default=False)),
                ('begin_time', models.CharField(max_length=5)),
                ('end_time', models.CharField(max_length=5)),
                ('building', models.CharField(max_length=6)),
                ('room', models.CharField(max_length=12)),
                ('Courses_pk', models.ForeignKey(to='courseapp.Courses')),
            ],
        ),
    ]
