# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-11 23:38
from __future__ import unicode_literals

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsignup',
            name='Contact_Number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128),
        ),
    ]
