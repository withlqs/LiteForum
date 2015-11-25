# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='comment',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='site',
            field=models.TextField(default=''),
        ),
    ]
