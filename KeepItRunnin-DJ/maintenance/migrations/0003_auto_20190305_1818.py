# Generated by Django 2.0.10 on 2019-03-06 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0002_auto_20190304_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance_record',
            name='date_completed',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='maintenance_record',
            name='next_due_date',
            field=models.DateField(),
        ),
    ]
