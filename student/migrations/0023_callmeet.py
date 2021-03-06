# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-07 13:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0022_auto_20180407_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallMeet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dati', models.DateTimeField()),
                ('agen', models.CharField(max_length=256)),
                ('rep', models.CharField(max_length=256)),
                ('ven', models.CharField(max_length=256)),
                ('cfrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
                ('cto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cto', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
