# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libm', '0004_remove_studentinfo_issued_book_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUpSt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('university_roll_no', models.IntegerField(default=None)),
                ('student_name', models.CharField(default=None, max_length=100)),
                ('password', models.CharField(default=None, max_length=100)),
                ('password_confirm', models.CharField(default=None, max_length=100)),
            ],
            bases=(models.Model, dict),
        ),
    ]
