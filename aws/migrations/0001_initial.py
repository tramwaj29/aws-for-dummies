# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField(default=None, max_length=128, null=True)),
            ],
        ),
    ]
