# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('catalogue', models.CharField(max_length=30)),
                ('record_date', models.DateTimeField(verbose_name=b'date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
