# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20151119_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='site',
            field=models.TextField(),
        ),
    ]
