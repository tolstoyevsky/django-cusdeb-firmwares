# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmwares', '0008_auto_20181211_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='firmware',
            name='notes',
            field=models.TextField(default=''),
        ),
    ]
