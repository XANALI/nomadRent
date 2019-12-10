# Generated by Django 2.2.6 on 2019-12-09 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourApp', '0008_auto_20191210_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='approves',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='canceled',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='finished',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
