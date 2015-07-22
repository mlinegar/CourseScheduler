# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses_location',
            old_name='Courses_pk',
            new_name='Courses',
        ),
    ]
