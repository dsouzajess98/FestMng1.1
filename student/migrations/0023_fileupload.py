# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-07 13:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0022_auto_20180407_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(upload_to=student.models.upload_to)),
                ('rid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Request', to_field='rid')),
            ],
        ),
    ]
