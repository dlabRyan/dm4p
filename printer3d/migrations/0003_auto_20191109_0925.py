# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-11-09 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printer3d', '0002_printer3d_manufacturer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(max_length=50)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('finish', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='printer3d',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]