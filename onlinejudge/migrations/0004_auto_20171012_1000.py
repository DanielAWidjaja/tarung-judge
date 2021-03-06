# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinejudge', '0003_auto_20171011_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='template',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='attempt',
            name='status',
            field=models.IntegerField(choices=[(0, 'Wrong Answer'), (1, 'Accepted'), (2, 'Runtime Error'), (3, 'Server Error'), (4, 'Timed Out'), (-1, 'Accepted (Testing)')]),
        ),
    ]
