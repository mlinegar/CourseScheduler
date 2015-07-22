# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0002_auto_20150722_0820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses_location',
            old_name='Courses',
            new_name='Course',
        ),
    ]
