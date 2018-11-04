# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-02 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_mustbuy_nav'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackid', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
                ('categoryid', models.CharField(max_length=8)),
                ('brandname', models.CharField(max_length=50)),
                ('img1', models.CharField(max_length=100)),
                ('childcid1', models.CharField(max_length=8)),
                ('productid1', models.CharField(max_length=8)),
                ('longname1', models.CharField(max_length=100)),
                ('price1', models.FloatField()),
                ('marketprice1', models.FloatField()),
                ('img2', models.CharField(max_length=100)),
                ('childcid2', models.CharField(max_length=8)),
                ('productid2', models.CharField(max_length=8)),
                ('longname2', models.CharField(max_length=100)),
                ('price2', models.FloatField()),
                ('marketprice2', models.FloatField()),
                ('img3', models.CharField(max_length=100)),
                ('childcid3', models.CharField(max_length=8)),
                ('productid3', models.CharField(max_length=8)),
                ('longname3', models.CharField(max_length=100)),
                ('price3', models.FloatField()),
                ('marketprice3', models.FloatField()),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'axf_shop',
            },
        ),
    ]
