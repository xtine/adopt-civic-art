# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-18 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0006_remove_artworkimage_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoption',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='date_entered',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='artworkimage',
            name='image',
            field=models.ImageField(blank=True, help_text='Image file upload size limit is 2.5MB.', upload_to='artworks/'),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]