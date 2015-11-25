# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=datetime.datetime(2015, 11, 18, 16, 41, 46, 728731, tzinfo=utc), unique=True, max_length=30),
            preserve_default=False,
        ),
    ]
