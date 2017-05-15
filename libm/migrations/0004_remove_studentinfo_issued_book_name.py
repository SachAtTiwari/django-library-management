# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libm', '0003_auto_20160529_0504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='issued_book_name',
        ),
    ]
