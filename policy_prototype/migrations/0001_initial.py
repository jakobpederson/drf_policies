# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-22 17:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liability', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_number', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ('policy_number',),
            },
        ),
        migrations.AddField(
            model_name='coverage',
            name='policy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coverages', to='policy_prototype.Policy'),
        ),
    ]
