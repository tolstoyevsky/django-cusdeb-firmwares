# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmwares', '0005_firmware_format'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=80)),
                ('short_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TargetDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=80)),
                ('short_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='firmware',
            name='distro',
            field=models.ForeignKey(to='firmwares.Distro', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='firmware',
            name='targetdevice',
            field=models.ForeignKey(to='firmwares.TargetDevice', blank=True, null=True),
        ),
    ]
