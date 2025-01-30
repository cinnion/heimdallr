from django.db import models
from django.db.models import Index
from netfields import CidrAddressField
from django.core.cache import caches

class filterlog(models.Model):
    timestamp = models.DateTimeField()
    hostname = models.CharField(max_length=32)
    rule_num = models.IntegerField()
    sub_rule = models.CharField(max_length=32, blank=True)
    anchor = models.CharField(max_length=64, blank=True)
    tracker = models.CharField(max_length=64, blank=True)
    interface = models.CharField(max_length=16)
    reason = models.CharField(max_length=16)
    action = models.CharField(max_length=16)
    direction = models.CharField(max_length=4)
    ip_version = models.SmallIntegerField()

    # IPv4 fields
    tos = models.CharField(max_length=8, null=True)
    ecn = models.CharField(max_length=8, null=True, blank=True)
    ttl = models.SmallIntegerField(null=True)
    pkt_id = models.IntegerField(null=True)
    pkt_offset = models.IntegerField(null=True)
    flags = models.CharField(max_length=32, null=True)

    # IPv6 fields
    pkt_class = models.CharField(max_length=8, null=True, blank=True)
    flow_label = models.CharField(max_length=8, null=True, blank=True)
    hop_limit = models.IntegerField(null=True)

    # Shared IPv4/IPv6 fields
    proto_id = models.IntegerField()
    protocol = models.CharField(max_length=16)
    pkt_length = models.IntegerField()
    source_ip = models.GenericIPAddressField()
    dest_ip = models.GenericIPAddressField()

    # Rest of the packet
    rest = models.JSONField()

    class Meta:
        db_table = 'filterlog'
        indexes = [
            Index(fields=['timestamp']),
            Index(fields=['source_ip']),
            Index(fields=['dest_ip']),
        ]

class Blackhole(models.Model):
    blackhole = CidrAddressField()

    class Meta:
        db_table = 'blacklist'

class heavyHitter(models.Model):
    cnt = models.IntegerField()
    tmstamp = models.DateTimeField()
    cidrBlock = CidrAddressField()
    rule_num = models.IntegerField()
    blocked = models.IntegerField()
    blocked_ports = models.IntegerField()
    bh_id = models.BigIntegerField()
    blackhole = CidrAddressField()

    class Meta:
        managed = False


