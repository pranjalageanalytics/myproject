# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-12-07 14:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gift_app', '0004_auto_20161205_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mychallengerelrel',
            name='challenge_join_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 14, 15, 27, 550000, tzinfo=utc)),
        ),
    ]
