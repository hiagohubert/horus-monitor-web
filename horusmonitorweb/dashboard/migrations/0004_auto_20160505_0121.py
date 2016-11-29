# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 01:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_os'),
    ]

    operations = [
        migrations.AddField(
            model_name='os',
            name='machine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Machine'),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='machine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Machine'),
        ),
    ]
