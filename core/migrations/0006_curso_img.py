# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20171106_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
