# Generated by Django 2.2.6 on 2019-12-08 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourApp', '0003_auto_20191208_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email_address',
            field=models.CharField(max_length=200),
        ),
    ]
