# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmwares', '0007_auto_20181208_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('full_name', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='firmware',
            name='build_type',
            field=models.ForeignKey(blank=True, null=True, to='firmwares.BuildType'),
        ),
    ]
