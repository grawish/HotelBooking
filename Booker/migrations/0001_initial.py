# Generated by Django 3.0.8 on 2020-07-27 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('h_id', models.AutoField(primary_key=True, serialize=False)),
                ('h_name', models.CharField(default='', max_length=50)),
                ('h_address', models.CharField(default='', max_length=100)),
                ('h_zipcode', models.CharField(default='', max_length=10)),
                ('h_contact', models.CharField(default='', max_length=10)),
                ('h_email', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('r_id', models.AutoField(primary_key=True, serialize=False)),
                ('r_no', models.IntegerField(default=-1, max_length=500)),
                ('r_price', models.IntegerField(default=-1)),
                ('r_bed', models.IntegerField(default=1)),
                ('r_view', models.CharField(default='N/A', max_length=50)),
                ('h_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booker.Hotel')),
            ],
        ),
    ]
