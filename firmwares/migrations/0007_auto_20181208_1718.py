# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmwares', '0006_auto_20180317_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firmware',
            name='format',
            field=models.CharField(max_length=6, choices=[('tar.gz', 'Old tar.gz'), ('img.gz', 'New img.gz'), ('mender', 'Mender artifact')], default='tar.gz'),
        ),
    ]
