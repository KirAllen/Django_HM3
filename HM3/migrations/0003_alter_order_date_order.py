# Generated by Django 4.2.5 on 2023-09-30 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_rename_passwod_customer_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_order',
            field=models.DateTimeField(),
        ),
    ]