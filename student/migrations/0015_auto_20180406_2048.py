# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-06 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_auto_20180406_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brmsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.IntegerField(unique=True)),
                ('msg', models.CharField(default='Important Message', max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='request',
            name='rid',
            field=models.IntegerField(unique=True),
        ),
    ]
