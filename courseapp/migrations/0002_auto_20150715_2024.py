# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='add_me',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='courses',
            name='days',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='courses',
            name='location',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='courses',
            name='time',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='courses',
            name='group',
            field=models.CharField(default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='courses',
            name='instructor',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='courses',
            name='note',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='courses',
            name='status',
            field=models.CharField(default='', max_length=9),
        ),
        migrations.AlterField(
            model_name='courses',
            name='subject',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='courses',
            name='term',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='courses',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='courses',
            name='xlist',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='courses',
            name='year',
            field=models.CharField(default='', max_length=4),
        ),
    ]
