# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_record_modified_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('catalogue', models.CharField(max_length=20)),
                ('level', models.IntegerField(default=5)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(default=datetime.datetime(2015, 2, 11, 23, 18, 14, 346000, tzinfo=utc), blank=True)),
                ('available', models.BooleanField(default=True)),
                ('borrower', models.ForeignKey(blank=True, to='books.Student', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='record',
            name='borrower',
        ),
        migrations.DeleteModel(
            name='Record',
        ),
    ]
