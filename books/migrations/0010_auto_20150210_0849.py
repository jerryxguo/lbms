# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20150210_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='author',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='catalogue',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='title',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
