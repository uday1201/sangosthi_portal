# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-10 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebPortal', '0022_qas_questionfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiofile',
            name='audioComposition',
            field=models.CharField(choices=[('single file', 'single file'), ('multiple file', 'multiple files')], max_length=100, null=True),
        ),
    ]
