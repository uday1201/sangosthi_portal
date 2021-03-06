# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-10 10:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebPortal', '0041_auto_20180410_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='answer1',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, related_name='answer1_audio', to='WebPortal.AudioFile'),
        ),
        migrations.AlterField(
            model_name='show',
            name='answer3',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, related_name='answer3_audio', to='WebPortal.AudioFile'),
        ),
        migrations.AlterField(
            model_name='show',
            name='question1',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, related_name='question1_audio', to='WebPortal.AudioFile'),
        ),
        migrations.AlterField(
            model_name='show',
            name='question3',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, related_name='question3_audio', to='WebPortal.AudioFile'),
        ),
    ]
