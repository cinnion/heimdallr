# Generated by Django 5.1.3 on 2024-12-08 01:35

import netfields.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blacklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blackhole', netfields.fields.CidrAddressField(max_length=43)),
            ],
            options={
                'db_table': 'blacklist',
            },
        ),
        migrations.CreateModel(
            name='filterlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('hostname', models.CharField(max_length=32)),
                ('rule_num', models.IntegerField()),
                ('sub_rule', models.CharField(blank=True, max_length=32)),
                ('anchor', models.CharField(blank=True, max_length=64)),
                ('tracker', models.CharField(blank=True, max_length=64)),
                ('interface', models.CharField(max_length=16)),
                ('reason', models.CharField(max_length=16)),
                ('action', models.CharField(max_length=16)),
                ('direction', models.CharField(max_length=4)),
                ('ip_version', models.SmallIntegerField()),
                ('tos', models.CharField(max_length=8, null=True)),
                ('ecn', models.CharField(blank=True, max_length=8, null=True)),
                ('ttl', models.SmallIntegerField(null=True)),
                ('pkt_id', models.IntegerField(null=True)),
                ('pkt_offset', models.IntegerField(null=True)),
                ('flags', models.CharField(max_length=32, null=True)),
                ('pkt_class', models.CharField(blank=True, max_length=8, null=True)),
                ('flow_label', models.CharField(blank=True, max_length=8, null=True)),
                ('hop_limit', models.IntegerField(null=True)),
                ('proto_id', models.IntegerField()),
                ('protocol', models.CharField(max_length=16)),
                ('pkt_length', models.IntegerField()),
                ('source_ip', models.GenericIPAddressField()),
                ('dest_ip', models.GenericIPAddressField()),
                ('rest', models.JSONField()),
            ],
            options={
                'db_table': 'filterlog',
                'indexes': [models.Index(fields=['timestamp'], name='filterlog_timesta_37454e_idx'), models.Index(fields=['source_ip'], name='filterlog_source__9ccd17_idx'), models.Index(fields=['dest_ip'], name='filterlog_dest_ip_95eaf5_idx')],
            },
        ),
    ]
