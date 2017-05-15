# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libm', '0005_signupst'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='fine',
            field=models.IntegerField(default=None),
        ),
    ]
