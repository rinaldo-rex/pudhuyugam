# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-04 16:49
from __future__ import unicode_literals

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('vidiyal', '0008_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
