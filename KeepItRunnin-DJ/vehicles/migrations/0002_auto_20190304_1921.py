# Generated by Django 2.0.10 on 2019-03-05 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='status',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]