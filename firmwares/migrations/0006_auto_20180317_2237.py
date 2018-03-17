# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firmwares', '0005_firmware_format'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distro',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('full_name', models.CharField(max_length=80)),
                ('short_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TargetDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('full_name', models.CharField(max_length=80)),
                ('short_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='firmware',
            name='distro',
            field=models.ForeignKey(to='firmwares.Distro', null=True, blank=True, to_field=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='firmware',
            name='targetdevice',
            field=models.ForeignKey(to='firmwares.TargetDevice', null=True, blank=True, to_field=django.db.models.deletion.SET_NULL),
        ),
    ]
