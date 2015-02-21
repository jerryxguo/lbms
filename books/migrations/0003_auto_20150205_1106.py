# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20150205_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='record_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
