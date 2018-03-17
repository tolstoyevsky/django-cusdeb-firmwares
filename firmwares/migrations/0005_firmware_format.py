# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmwares', '0004_firmware_pro_only'),
    ]

    operations = [
        migrations.AddField(
            model_name='firmware',
            name='format',
            field=models.CharField(choices=[('tar.gz', 'Old tar.gz'), ('img.gz', 'New img.gz')], max_length=6, default='tar.gz'),
        ),
    ]
