# Generated by Django 2.0.10 on 2019-03-01 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_auto_20190301_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='driveWheels',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='transmission',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]