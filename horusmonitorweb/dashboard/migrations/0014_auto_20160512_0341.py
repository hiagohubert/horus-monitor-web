# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-12 03:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='inserted_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Inserido em'),
        ),
        migrations.AddField(
            model_name='service',
            name='machine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Machine'),
        ),
        migrations.AddField(
            model_name='service',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Atualizado em'),
        ),
    ]
