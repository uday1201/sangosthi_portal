# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-25 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebPortal', '0009_content_localized'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='show_stats',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to='uploads/show_stats/'),
        ),
    ]
