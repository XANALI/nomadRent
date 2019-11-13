# Generated by Django 2.2.6 on 2019-11-13 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourApp', '0002_simpleuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('power', models.FloatField(default=0)),
                ('consummation', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userImg', models.ImageField(default='NULL', upload_to='car_pictures/')),
            ],
        ),
        migrations.CreateModel(
            name='ModelOfCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
