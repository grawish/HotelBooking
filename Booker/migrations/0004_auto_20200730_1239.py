# Generated by Django 3.0.8 on 2020-07-30 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booker', '0003_booking_b_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='b_A',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='booking',
            name='b_C',
            field=models.IntegerField(default=0),
        ),
    ]