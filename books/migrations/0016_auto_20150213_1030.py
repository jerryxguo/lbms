# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_auto_20150212_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='borrower',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, to='books.Student', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='collection',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 12, 23, 30, 50, 782000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
