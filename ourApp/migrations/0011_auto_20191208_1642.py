# Generated by Django 2.2.6 on 2019-12-08 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ourApp', '0010_auto_20191208_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simpleuser',
            name='bank_card_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ourApp.BankCard'),
        ),
        migrations.AlterField(
            model_name='simpleuser',
            name='license_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ourApp.DriverLicense'),
        ),
    ]
