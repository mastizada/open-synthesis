# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_title', models.CharField(max_length=200)),
                ('board_desc', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evidence_url', models.URLField()),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openach.Board')),
            ],
        ),
        migrations.CreateModel(
            name='Hypothesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hypothesis_text', models.CharField(max_length=200)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openach.Board')),
            ],
        ),
    ]