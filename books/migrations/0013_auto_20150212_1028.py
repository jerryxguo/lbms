# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_auto_20150212_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='schoolClass',
            field=models.ForeignKey(blank=True, to='books.Class', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='collection',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 11, 23, 28, 33, 77000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
