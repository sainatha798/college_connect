# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-29 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postfeed', '0007_auto_20171029_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='post',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='postfeed.Post'),
        ),
        migrations.AlterField(
            model_name='userprefernces',
            name='tags',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='postfeed.Tag'),
        ),
    ]