# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default=b'admin', max_length=100)),
                ('password', models.CharField(default=b'admin', max_length=100)),
            ],
            bases=(models.Model, dict),
        ),
        migrations.CreateModel(
            name='AvailableBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_name', models.CharField(default=None, max_length=100)),
                ('Author_name', models.CharField(default=None, max_length=100)),
            ],
            bases=(models.Model, dict),
        ),
        migrations.CreateModel(
            name='IssuedBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_name', models.CharField(default=None, max_length=100)),
                ('Author_name', models.CharField(default=None, max_length=100)),
                ('assignedTo', models.CharField(default=None, max_length=100)),
                ('lendPeriod_to', models.DateTimeField(default=None, max_length=100)),
                ('lendPeriod_from', models.DateTimeField(default=None, max_length=100)),
            ],
            bases=(models.Model, dict),
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_name', models.CharField(default=None, max_length=100)),
                ('student_department', models.CharField(default=None, max_length=100)),
                ('book_issued', models.CharField(default=None, max_length=100)),
            ],
            bases=(models.Model, dict),
        ),
    ]
