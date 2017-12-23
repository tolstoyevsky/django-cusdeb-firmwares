# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmwares', '0003_auto_20170305_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='firmware',
            name='pro_only',
            field=models.BooleanField(default=False),
        ),
    ]
