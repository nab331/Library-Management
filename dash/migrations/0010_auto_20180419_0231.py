# Generated by Django 2.0.4 on 2018-04-18 21:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0009_book_bookinstance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='due_back',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 5, 4, 2, 31, 2, 577561), null=True),
        ),
    ]