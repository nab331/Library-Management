# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-20 02:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0013_auto_20180419_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='due_back',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 5, 5, 7, 48, 44, 297148), null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='userType',
            field=models.CharField(choices=[(b'student', b'student'), (b'staff', b'staff'), (b'admin', b'admin')], max_length=100),
        ),
    ]
