# Generated by Django 2.2.6 on 2019-11-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourApp', '0002_auto_20191128_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simpleuser',
            name='userImg',
            field=models.ImageField(default='/default.jpg', upload_to='user_avas/'),
        ),
    ]
