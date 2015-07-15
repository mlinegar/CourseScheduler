# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('CRN', models.CharField(primary_key=True, serialize=False, max_length=5)),
                ('term', models.CharField(max_length=10)),
                ('year', models.DateField()),
                ('note', models.CharField(max_length=250)),
                ('course', models.CharField(max_length=12)),
                ('title', models.CharField(max_length=50)),
                ('xlist', models.CharField(max_length=12)),
                ('instructor', models.CharField(max_length=30)),
                ('group', models.CharField(max_length=1)),
                ('graduate_level', models.BooleanField(default=False)),
                ('year_long', models.BooleanField(default=False)),
                ('subject', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=9)),
                ('units', models.DecimalField(max_digits=3, decimal_places=1)),
            ],
        ),
    ]
