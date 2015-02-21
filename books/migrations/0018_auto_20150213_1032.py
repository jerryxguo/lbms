# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_auto_20150213_1030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Number',
            new_name='schoolClass',
        ),
        migrations.AlterField(
            model_name='collection',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 12, 23, 32, 14, 448000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
