# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-12 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20180612_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citydict',
            name='desc',
            field=models.CharField(max_length=200, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='desc',
            field=models.TextField(verbose_name='\u673a\u6784\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(upload_to='org/%Y/%m', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u673a\u6784\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='', upload_to='teacher/%Y/%m', verbose_name='\u5934\u50cf'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u6559\u5e08\u540d\u79f0'),
        ),
    ]
