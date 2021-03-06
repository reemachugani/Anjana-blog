# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-22 04:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Singlepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Max 250 characters', max_length=250)),
                ('slug', models.SlugField(help_text='Suggested value automatically generated from title. Must be unique.')),
                ('display_word', models.CharField(help_text='Max 50 characters. Displayed in the header.', max_length=50)),
                ('body', models.TextField()),
                ('body_html', models.TextField(blank=True, editable=False)),
            ],
        ),
    ]
