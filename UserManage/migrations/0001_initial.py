# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='M_USER',
            fields=[
                ('USER_ID', models.AutoField(primary_key=True, serialize=False)),
                ('USER_NAME', models.CharField(max_length=32)),
                ('IS_ACTIVE', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'm_user',
            },
        ),
    ]
