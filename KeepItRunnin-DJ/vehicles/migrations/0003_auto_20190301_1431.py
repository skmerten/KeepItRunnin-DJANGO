# Generated by Django 2.0.10 on 2019-03-01 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_vehicle_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='mpg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='tankSize',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='trim',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
