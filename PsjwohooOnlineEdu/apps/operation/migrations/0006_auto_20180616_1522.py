# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-16 15:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_teacher'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0005_auto_20180614_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecomments',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='\u8bfe\u7a0b'),
        ),
        migrations.AddField(
            model_name='coursecomments',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237'),
        ),
    ]
