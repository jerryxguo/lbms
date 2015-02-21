# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20150212_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='borrower',
        ),
        migrations.AlterField(
            model_name='collection',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 12, 5, 56, 59, 923000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
