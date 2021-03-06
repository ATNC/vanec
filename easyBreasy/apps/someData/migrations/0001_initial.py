# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 21:56
from __future__ import unicode_literals

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
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_image', models.ImageField(upload_to='client/photos/')),
                ('client_description', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents_file', models.FileField(upload_to='client/documents/')),
                ('documents_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docs', to='someData.Client')),
            ],
        ),
    ]
