# Generated by Django 2.0.10 on 2019-02-16 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20190215_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]