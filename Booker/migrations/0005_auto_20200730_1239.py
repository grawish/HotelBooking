# Generated by Django 3.0.8 on 2020-07-30 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booker', '0004_auto_20200730_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='r_no',
            field=models.IntegerField(default=-1),
        ),
    ]
