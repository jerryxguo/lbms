# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20150210_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 10, 7, 8, 32, 257000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
