# Generated by Django 2.2.8 on 2019-12-06 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0074_invoice_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='telephone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]