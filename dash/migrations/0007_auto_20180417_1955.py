# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0006_auto_20180417_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='userName',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dash.Type'),
        ),
    ]
