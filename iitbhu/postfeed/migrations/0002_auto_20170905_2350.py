# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 18:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postfeed', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
