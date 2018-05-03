# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-09 10:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebPortal', '0015_auto_20180409_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qas',
            name='content',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='WebPortal.Content'),
        ),
        migrations.AlterField(
            model_name='qas',
            name='questionFile',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='WebPortal.AudioFile'),
        ),
    ]
