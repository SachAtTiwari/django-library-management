# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libm', '0006_studentinfo_fine'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUpT',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eid', models.IntegerField(default=None)),
                ('t_name', models.CharField(default=None, max_length=100)),
                ('password', models.CharField(default=None, max_length=100)),
                ('password_confirm', models.CharField(default=None, max_length=100)),
            ],
            bases=(models.Model, dict),
        ),
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('t_name', models.CharField(default=None, max_length=100)),
                ('eid', models.IntegerField(default=None)),
                ('teacher_department', models.CharField(default=None, max_length=100)),
                ('no_of_books_issued', models.IntegerField(default=None)),
                ('fine', models.IntegerField(default=None)),
            ],
            bases=(models.Model, dict),
        ),
    ]
