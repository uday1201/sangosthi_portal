# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-10 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebPortal', '0023_audiofile_audiocomposition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audiofile',
            name='audioComposition',
        ),
        migrations.AddField(
            model_name='show',
            name='question1',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='WebPortal.AudioFile'),
        ),
    ]
