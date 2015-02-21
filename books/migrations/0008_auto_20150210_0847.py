# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_record_borrower'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='record_date',
            new_name='create_date',
        ),
    ]
