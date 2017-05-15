# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libm', '0002_auto_20160529_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='lendPeriod_from',
            field=models.DateField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='lendPeriod_to',
            field=models.DateField(default=None, max_length=100),
        ),
    ]
