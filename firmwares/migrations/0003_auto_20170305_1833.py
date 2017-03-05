# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmwares', '0002_auto_20161224_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firmware',
            name='status',
            field=models.CharField(max_length=11, default='done', choices=[('done', 'Done'), ('failed', 'Failed'), ('building', 'Building'), ('initialized', 'Initialized')]),
        ),
    ]
