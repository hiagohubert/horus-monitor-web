# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 01:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('architecture', models.CharField(max_length=100, verbose_name='Arquitetura')),
                ('vendor_id', models.CharField(max_length=100, verbose_name='Vendor')),
                ('model_name', models.CharField(max_length=100, verbose_name='Modelo')),
            ],
        ),
        migrations.AlterField(
            model_name='machine',
            name='token',
            field=models.UUIDField(editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='cpu',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Machine'),
        ),
    ]
