# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_record_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='level',
            field=models.IntegerField(default=5),
            preserve_default=True,
        ),
    ]
