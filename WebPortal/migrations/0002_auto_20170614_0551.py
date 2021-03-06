# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 00:21
from __future__ import unicode_literals

import WebPortal.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebPortal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='audioFor',
            field=models.CharField(choices=[('content', 'content'), ('trailer', 'trailer')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='showfeedback',
            name='feedbackFile',
            field=models.FileField(max_length=200, null=True, upload_to='uploads/show_feedback/', validators=[WebPortal.validators.validate_audiofile_extension]),
        ),
    ]
