# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-07 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170807_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='ass',
            field=models.CharField(default='aaa', max_length=100),
        ),
    ]
