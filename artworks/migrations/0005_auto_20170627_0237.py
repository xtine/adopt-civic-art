# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0004_auto_20170626_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artworkimage',
            name='image',
            field=models.ImageField(blank=True, upload_to='artworks/'),
        ),
        migrations.AlterField(
            model_name='checkinimage',
            name='image',
            field=models.ImageField(upload_to='checkins/'),
        ),
    ]