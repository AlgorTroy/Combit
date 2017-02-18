# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobApp', '0003_job_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AddField(
            model_name='job',
            name='payment',
            field=models.IntegerField(default=0),
        ),
    ]
