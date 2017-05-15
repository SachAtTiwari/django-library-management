# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinfo',
            old_name='book_issued',
            new_name='issued_book_name',
        ),
        migrations.RemoveField(
            model_name='issuedbook',
            name='Author_name',
        ),
        migrations.AddField(
            model_name='availablebook',
            name='Department',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='issuedbook',
            name='roll_no',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='no_of_books_issued',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='university_roll_no',
            field=models.IntegerField(default=None),
        ),
    ]
