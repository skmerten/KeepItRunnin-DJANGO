# Generated by Django 2.0.10 on 2019-02-28 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='color',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]