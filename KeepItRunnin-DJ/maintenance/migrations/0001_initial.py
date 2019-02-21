# Generated by Django 2.0.10 on 2019-02-13 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100, null=True)),
                ('months', models.IntegerField()),
                ('miles', models.IntegerField()),
                ('materials', models.CharField(max_length=250, null=True)),
                ('comments', models.CharField(max_length=250, null=True)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.Vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance_History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=250)),
                ('date_completed', models.DateTimeField()),
                ('current_mileage', models.IntegerField()),
                ('next_due_date', models.DateTimeField()),
                ('next_due_mile', models.IntegerField()),
                ('completed', models.IntegerField()),
                ('maintenance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.Maintenance')),
            ],
        ),
    ]