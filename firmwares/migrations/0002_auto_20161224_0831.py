# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmwares', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='firmware',
            name='finished_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='firmware',
            name='log',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='firmware',
            name='started_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='firmware',
            name='status',
            field=models.CharField(default='done', choices=[('done', 'Done'), ('failed', 'Failed'), ('building', 'Building')], max_length=8),
        ),
    ]
