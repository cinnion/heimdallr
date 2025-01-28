# Generated by Django 5.1.3 on 2024-12-23 18:40

import netfields.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firewall', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='heavyHitters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnt', models.IntegerField()),
                ('tmstamp', models.DateTimeField()),
                ('cidrBlock', netfields.fields.CidrAddressField(max_length=43)),
                ('bh_id', models.BigIntegerField()),
                ('blackhole', netfields.fields.CidrAddressField(max_length=43)),
            ],
            options={
                'managed': False,
            },
        ),
    ]
