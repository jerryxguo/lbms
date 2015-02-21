# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20150210_0847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='create_date',
            new_name='creation_date',
        ),
    ]
