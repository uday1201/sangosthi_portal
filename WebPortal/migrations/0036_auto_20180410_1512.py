# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-10 09:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebPortal', '0035_auto_20180410_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='answer1',
        ),
        migrations.RemoveField(
            model_name='show',
            name='answer2',
        ),
        migrations.RemoveField(
            model_name='show',
            name='answer3',
        ),
        migrations.RemoveField(
            model_name='show',
            name='question1',
        ),
        migrations.RemoveField(
            model_name='show',
            name='question2',
        ),
        migrations.RemoveField(
            model_name='show',
            name='question3',
        ),
    ]
