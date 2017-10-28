# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidiyal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='desc',
            field=models.CharField(default='Bridging the gap between the ones who need, and the ones who provide...', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='idea',
            name='description',
            field=models.TextField(max_length=20000),
        ),
    ]
