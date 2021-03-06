# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 17:47
from __future__ import unicode_literals

import WebPortal.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebPortal', '0004_auto_20170615_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowRecording',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recordingFile', models.FileField(max_length=200, null=True, upload_to='uploads/show_recordings/', validators=[WebPortal.validators.validate_audiofile_extension])),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='showrecording_create', to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('show', models.ForeignKey(help_text='Select a show from the dropdown', null=True, on_delete=django.db.models.deletion.CASCADE, to='WebPortal.Show')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='showrecording_update', to=settings.AUTH_USER_MODEL, verbose_name='last updated by')),
            ],
        ),
    ]
