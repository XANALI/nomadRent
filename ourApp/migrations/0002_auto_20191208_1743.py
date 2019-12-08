# Generated by Django 2.2.6 on 2019-12-08 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ourApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simpleuser',
            name='bank_card_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ourApp.BankCard'),
        ),
        migrations.AlterField(
            model_name='simpleuser',
            name='license_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ourApp.DriverLicense'),
        ),
    ]