from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from firewall.models import heavyHitters
from django.core.cache import cache

class Command(BaseCommand):
    help = 'Generate a list of CIDR blocks making lots of requests.'

    def handle(self, *args, **options):

        hitters = heavyHitters.objects.raw("""
SELECT cnt, fw.tm as tmstamp, fw.net as cidrBlock, rule_num, blocked, blocked_ports, id as bh_id, blackhole
FROM (
    SELECT COUNT(*) as cnt, DATE_TRUNC('day', timestamp) as tm, NETWORK(SET_MASKLEN(source_ip,24)) AS net, MAX(rule_num) as rule_num
    FROM filterlog
    WHERE direction='in'
      AND NOT (source_ip << '192.168.8.0/20')
      AND NOT source_ip = '216.66.22.2'
      AND NOT source_ip = '0.0.0.0'
      AND ip_version = '4'
      AND interface = 'em1'
    GROUP BY net, DATE_TRUNC('day', timestamp)
) AS fw
LEFT OUTER JOIN (
    SELECT DATE_TRUNC('day', timestamp) as tm, NETWORK(SET_MASKLEN(source_ip,24)) AS net, count(*) AS blocked, COUNT(DISTINCT rest::json->>'dport') AS blocked_ports
    FROM filterlog
    WHERE direction='in'
      AND NOT (source_ip << '192.168.8.0/20')
      AND NOT source_ip = '216.66.22.2'
      AND NOT source_ip = '0.0.0.0'
      AND ip_version = '4'
      AND interface = 'em1'
      AND action = 'block'
      AND protocol IN ('tcp', 'udp')
    GROUP BY net, DATE_TRUNC('day', timestamp)

) AS blocks ON (fw.tm = blocks.tm and fw.net = blocks.net)
LEFT OUTER JOIN blacklist ON (fw.net <<= blackhole)
WHERE cnt > 100
ORDER BY cnt DESC                                           
                                           """)

        cache.set("heavyHitters", hitters)
