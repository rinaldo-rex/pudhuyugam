# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-28 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidiyal', '0004_auto_20171028_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('desc', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=20000)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]