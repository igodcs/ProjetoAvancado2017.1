# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20171027_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='tipo',
            field=models.CharField(max_length=14, null=True),
        ),
    ]