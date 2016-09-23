# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 19:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('coast', models.DecimalField(decimal_places=2, max_digits=10)),
                ('model', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.DecimalField(decimal_places=2, max_digits=4)),
                ('width', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='instrument',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusShop.Manufacturer'),
        ),
        migrations.AddField(
            model_name='instrument',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusShop.Size'),
        ),
        migrations.AddField(
            model_name='instrument',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusShop.Type'),
        ),
    ]
