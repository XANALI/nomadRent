# Generated by Django 2.2.6 on 2019-12-08 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourApp', '0008_auto_20191207_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelofcar',
            name='modelImg',
            field=models.ImageField(default='/static/car/car-default.jpg', upload_to='car_pictures/'),
        ),
    ]
