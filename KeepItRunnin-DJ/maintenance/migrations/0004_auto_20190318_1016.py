# Generated by Django 2.0.10 on 2019-03-18 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0003_auto_20190305_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oilchange',
            name='vehicle',
        ),
        migrations.DeleteModel(
            name='OilChange',
        ),
    ]
