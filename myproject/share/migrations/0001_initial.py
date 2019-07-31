# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('Filesie', models.CharField(max_length=10)),
                ('path', models.CharField(max_length=32)),
                ('Datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('code', models.CharField(max_length=8)),
                ('DownloadDocount', models.IntegerField(default=0)),
                ('PCIP', models.CharField(max_length=32)),
            ],
        ),
    ]
