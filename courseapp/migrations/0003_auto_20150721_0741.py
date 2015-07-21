# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0002_auto_20150715_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='days',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=12), size=None),
        ),
        migrations.AlterField(
            model_name='courses',
            name='group',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1), size=None),
        ),
        migrations.AlterField(
            model_name='courses',
            name='location',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=12), size=None),
        ),
        migrations.AlterField(
            model_name='courses',
            name='time',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=12), size=None),
        ),
        migrations.AlterField(
            model_name='courses',
            name='xlist',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=12), size=None),
        ),
    ]
