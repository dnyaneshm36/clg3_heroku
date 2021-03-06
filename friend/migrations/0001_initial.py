# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-11 17:25
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Myfrienddetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('nick_name', models.CharField(blank=True, max_length=10, null=True)),
                ('date_of_birth', models.DateField(default=datetime.date.today)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'My friend detail',
                'verbose_name_plural': 'My friends  details',
            },
        ),
    ]
