# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-09 11:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebPortal', '0017_auto_20180409_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qas',
            name='QAID',
        ),
        migrations.RemoveField(
            model_name='qas',
            name='content',
        ),
        migrations.RemoveField(
            model_name='qas',
            name='questionFile',
        ),
    ]
