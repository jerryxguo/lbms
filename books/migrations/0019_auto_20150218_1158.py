# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0018_auto_20150213_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='schoolClass',
            new_name='school_class',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='LastName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='firstName',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='schoolClass',
            new_name='school_class',
        ),
        migrations.AlterField(
            model_name='collection',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 18, 0, 58, 8, 970000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
