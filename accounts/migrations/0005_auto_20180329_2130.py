# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-29 16:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180328_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsignup',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
