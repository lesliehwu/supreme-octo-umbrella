# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0002_auto_20170926_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='notes'),
            preserve_default=False,
        ),
    ]
