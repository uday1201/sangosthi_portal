# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-10 09:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebPortal', '0036_auto_20180410_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='answer1',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='answer1_audio', to='WebPortal.AudioFile'),
        ),
        migrations.AddField(
            model_name='show',
            name='answer2',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='answer2_audio', to='WebPortal.AudioFile'),
        ),
        migrations.AddField(
            model_name='show',
            name='answer3',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='answer3_audio', to='WebPortal.AudioFile'),
        ),
        migrations.AddField(
            model_name='show',
            name='question1',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='question1_audio', to='WebPortal.AudioFile'),
        ),
        migrations.AddField(
            model_name='show',
            name='question2',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='question2_audio', to='WebPortal.AudioFile'),
        ),
        migrations.AddField(
            model_name='show',
            name='question3',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='question3_audio', to='WebPortal.AudioFile'),
        ),
    ]
