# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-05 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidiyal', '0009_auto_20171104_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='img_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
