# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 04:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20160507_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpu',
            name='inserted_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Inserido em'),
        ),
    ]
