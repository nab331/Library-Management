# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0007_auto_20180417_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='userName',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
