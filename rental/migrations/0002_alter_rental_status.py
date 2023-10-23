# Generated by Django 4.2.6 on 2023-10-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='status',
            field=models.CharField(choices=[('CONFIRMED', 'Confirmed'), ('RENTED', 'Rented'), ('RETURNED', 'Returned'), ('CANCELLED', 'Cancelled'), ('RESERVED', 'Reserved')], default='CONFIRMED', max_length=20),
        ),
    ]