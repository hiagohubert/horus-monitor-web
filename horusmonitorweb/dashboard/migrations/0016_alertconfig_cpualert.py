# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 12:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20160512_0341'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_warning', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Máximo Atenção')),
                ('max_critical', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Máximo Critico')),
                ('alert_type', models.IntegerField(choices=[(1, 'CPU'), (2, 'Memory'), (3, 'Disc')], verbose_name='Tipo de Alerta')),
                ('machine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Machine')),
            ],
        ),
        migrations.CreateModel(
            name='CPUAlert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
