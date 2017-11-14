# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-updated']},
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='random'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='post_images'),
        ),
    ]