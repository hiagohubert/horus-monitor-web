# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-09 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20160507_0506'),
    ]

    operations = [
        migrations.AddField(
            model_name='disc',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Atualizado em'),
        ),
    ]
