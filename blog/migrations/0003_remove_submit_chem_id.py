# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 02:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170328_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submit',
            name='Chem_ID',
        ),
    ]
