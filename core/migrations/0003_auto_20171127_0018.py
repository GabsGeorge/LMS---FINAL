# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171127_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='apelido',
            field=models.CharField(db_column='Apelido', max_length=30, unique=True, verbose_name='Apelido'),
        ),
    ]