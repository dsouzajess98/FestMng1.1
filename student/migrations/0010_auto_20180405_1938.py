# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-05 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20180405_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuser',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='fuser',
            name='yofstudy',
        ),
        migrations.AddField(
            model_name='fuser',
            name='core',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='fuser',
            name='filter',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='fuser',
            name='subc',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
