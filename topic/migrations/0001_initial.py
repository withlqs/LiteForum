# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('name', models.CharField(max_length=20, unique=True)),
                ('codename', models.CharField(primary_key=True, max_length=20, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('content', models.TextField(max_length=20000)),
                ('pub_date', models.DateTimeField(null=True)),
                ('author', models.ForeignKey(null=True, to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=20000, null=True)),
                ('pub_date', models.DateTimeField(null=True)),
                ('upd_date', models.DateTimeField(null=True)),
                ('author', models.ForeignKey(null=True, to='user.User')),
                ('node', models.ForeignKey(null=True, to='topic.Node')),
            ],
        ),
        migrations.AddField(
            model_name='reply',
            name='reply_to',
            field=models.ForeignKey(null=True, to='topic.Topic'),
        ),
    ]
