# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-07 13:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ('-timestamp',)},
        ),
    ]
