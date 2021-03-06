# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-12-05 14:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gift_app', '0003_auto_20161129_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserChallengeCategoryLocationRelRelLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'user_challenge_category_location_rel_rel_locationtype',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='mychallengerelrel',
            name='challenge_join_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 5, 14, 38, 52, 448000, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='mychallengerelrel',
            name='status',
            field=models.ForeignKey(blank=True, db_column='status', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gift_app.StatusType'),
        ),
        migrations.AddField(
            model_name='mychallengerelrel',
            name='user',
            field=models.ForeignKey(blank=True, db_column='user', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gift_app.AuthUserGroups'),
        ),
        migrations.AddField(
            model_name='mychallengerelrel',
            name='user_challenge_category_location',
            field=models.ForeignKey(blank=True, db_column='user_challenge_category_location', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gift_app.UserChallengeCategoryLocationRelRel'),
        ),
        migrations.AlterField(
            model_name='mychallengerelrel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='userchallengecategorylocationrelrelcategory',
            table='user_challenge_category_location_rel_rel_categorytype',
        ),
    ]
