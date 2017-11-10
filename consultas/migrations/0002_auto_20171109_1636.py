# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='data',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='consulta',
            name='hora',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='codigo',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medico', to='usuarios.UserProfile'),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='usuarios.UserProfile'),
        ),
    ]