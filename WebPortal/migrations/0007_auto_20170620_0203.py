# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 20:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('WebPortal', '0006_auto_20170616_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='preFeedback',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='cohort', chained_model_field='cohort', help_text='The latest audio feedback of the show selected in this dropdown will be played when the current show starts.', null=True, on_delete=django.db.models.deletion.CASCADE, to='WebPortal.Show'),
        ),
        migrations.AddField(
            model_name='showfeedback',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='showfeedback',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='content',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='category', chained_model_field='category', null=True, on_delete=django.db.models.deletion.CASCADE, to='WebPortal.Content', verbose_name='Topic'),
        ),
        migrations.AlterField(
            model_name='show',
            name='status',
            field=models.IntegerField(choices=[(0, 'Due'), (1, 'Done')], default=0),
        ),
    ]
