# Generated by Django 2.2.6 on 2019-11-13 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourApp', '0005_auto_20191114_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalEquipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]