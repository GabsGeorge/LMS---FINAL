# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 03:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_cadastro_boletim'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cadastro_boletim',
            old_name='nome_aluno',
            new_name='ra',
        ),
    ]