# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-30 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DepUpdate', '0008_auto_20180312_0444'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthFaculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FID', models.CharField(max_length=8, unique=True)),
                ('Name', models.CharField(max_length=50)),
                ('Department', models.CharField(choices=[('aero', 'Aerospace'), ('civil', 'Civil'), ('cse', 'Computer Science'), ('ece', 'Electronics & Communication'), ('elec', 'Electrical'), ('mech', 'Mechanical'), ('meta', 'Materials & Metallurgical'), ('prod', 'Production & Industrial')], default='aero', max_length=4)),
                ('Designation', models.CharField(choices=[('prof', 'Professor'), ('asso', 'Associate Professor'), ('assi', 'Assistant Professor'), ('inst', 'Instructor')], default='prof', max_length=4)),
            ],
        ),
    ]
