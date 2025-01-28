from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from firewall.models import heavyHitters
from django.core.cache import cache

class Command(BaseCommand):
    help = 'Generate a list of CIDR blocks making lots of requests.'

    def handle(self, *args, **options):

        hitters = heavyHitters.objects.raw("""
SELECT cnt, tm, net, id as bh_id, blackhole
FROM (    
    SELECT COUNT(*) as cnt, DATE_TRUNC('day', timestamp) as tm, NETWORK(SET_MASKLEN(source_ip,24)) AS net
    FROM filterlog
    WHERE direction='in'
      AND NOT (source_ip << '192.168.8.0/20')
      AND NOT source_ip = '216.66.22.2'
      AND NOT source_ip = '0.0.0.0'
      AND ip_version = '4'
      AND interface = 'em1'
    GROUP BY net, DATE_TRUNC('day', timestamp)
) AS fw
LEFT OUTER JOIN blacklist ON (net <<= blackhole)
WHERE cnt > 100
ORDER BY cnt DESC                                           
                                           """)

        cache.set("heavyHitters", hitters)
