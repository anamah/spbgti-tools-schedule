# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20160605_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='classrecord',
            name='teacher',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='classrecord',
            name='class_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название занятия'),
        ),
        migrations.AlterField(
            model_name='classrecord',
            name='place',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Место проведения'),
        ),
    ]
