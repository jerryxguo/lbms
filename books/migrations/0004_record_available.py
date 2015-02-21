# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20150205_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='available',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
