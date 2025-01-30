from typing import List, Optional

from django.db.models.query import RawQuerySet
from django.shortcuts import render
from django.http import HttpResponse
from .models import Blackhole, heavyHitter

from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import BlackholeSerializer, HeavyHittersSerializer
from datetime import date

def menu(request) -> HttpResponse:
    return render(request, 'main.html')

def blackholes(request) -> HttpResponse:
    return render(request, 'blackholes.html')

def heavy_hitters_list(request) -> HttpResponse:
    return render(request, 'HeavyHittersList.html')

class Blackholes(generics.GenericAPIView):
    serializer_class = BlackholeSerializer
    queryset = Blackhole.objects.all()

    def get_sort(self, request) -> Optional[List[str]]:
        """
        Parse the request to get the ordering information and return it in a Django compliant list.
        The method returns None if there is no sorting requested.

        :param request:
        :return:
        """
        sort_order = []
        i = 0
        name = request.GET.get("order[%i][name]" % i)
        while name is not None:
            direction = request.GET.get("order[%i][dir]" % i)
            if direction == 'desc':
                sort_order.append('-' + name)
            else:
                sort_order.append(name)
            i += 1
            name = request.GET.get("order[%i][name]" % i)

        if len(sort_order) == 0:
            sort_order = None

        return sort_order

    def get(self, request):
        draw = int(request.GET.get("draw", 1))
        start_num = int(request.GET.get("start", 1))
        length = int(request.GET.get("length", 10))
        end_num = start_num + length
        search_param = request.GET.get("search[value]")
        blackholes = Blackhole.objects.all()
        total_applications = blackholes.count()
        total_filtered = total_applications
        sort_order = self.get_sort(request)

        if search_param:
            blackholes = blackholes.filter(company__icontains=search_param)
            total_filtered = blackholes.count()

        if sort_order:
            blackholes = blackholes.order_by(*sort_order)

        serializer = self.serializer_class(blackholes[start_num:end_num], many=True)

        return Response(
            {
                "status": "success",
                "draw": draw,
                "recordsTotal": total_applications,
                "recordsFiltered": total_filtered,
                "blackholes": serializer.data,
            }
        )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['when'] = date.today()
            serializer.save()
            return Response(
                {
                    "status": "success",
                    "blackhole": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {
                    "status": "fail",
                    "message": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class BlackholeDetail(generics.GenericAPIView):
    serializer_class = BlackholeSerializer
    queryset = Blackhole.objects.all()

    def get_blackhole(self, pk):
        try:
            return Blackhole.objects.get(pk=pk)
        except Exception:
            return None

    def get(self, request, pk):
        blackhole = self.get_blackhole(pk=pk)
        if blackhole is None:
            return Response(
                {
                    "status": "fail",
                    "message": f"Blackhole with Id: {pk} not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(blackhole)
        return Response(
            {
                "status": "success",
                "blackhole": serializer.data,
            }
        )

    def patch(self, request, pk):
        blackhole = self.get_blackhole(pk=pk)
        if blackhole is None:
            return Response(
                {
                    "status": "fail",
                    "message": f"Blackhole with Id: {pk} not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success",
                    "blackhole": serializer.data,
                },
            )
        else:
            return Response(
                {
                    "status": "fail",
                    "message": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        blackhole = self.get_blackhole(pk=pk)
        if blackhole is None:
            return Response(
                {
                    "status": "fail",
                    "message": f"Blackhole with Id: {pk} not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        blackhole.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HeavyHitters(generics.GenericAPIView):

    serializer_class = HeavyHittersSerializer
    queryset = None

    def __init__(self):
        super().__init__()
        self.queryset = self.custom_query_view()

    def custom_query_view(self) -> RawQuerySet:

        heavy_hitters = heavyHitter.objects.raw("""
    SELECT cnt, fw.tm as tm, fw.net as net, rule_num, blocked, blocked_ports, id as bh_id, blackhole
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

        return heavy_hitters

    def get_sort(self, request) -> Optional[List[str]]:
        """
        Parse the request to get the ordering information and return it in a Django compliant list.
        The method returns None if there is no sorting requested.

        :param request:
        :return:
        """
        sort_order = []
        i = 0
        name = request.GET.get("order[%i][name]" % i)
        while name is not None:
            direction = request.GET.get("order[%i][dir]" % i)
            if direction == 'desc':
                sort_order.append('-' + name)
            else:
                sort_order.append(name)
            i += 1
            name = request.GET.get("order[%i][name]" % i)

        if len(sort_order) == 0:
            sort_order = None

        return sort_order

    def get(self, request) -> Response:
        draw = int(request.GET.get("draw", 1))
        start_num = int(request.GET.get("start", 1))
        length = int(request.GET.get("length", 10))
        end_num = start_num + length
        search_param = request.GET.get("search[value]")
        heavy_hitters = self.custom_query_view()
        total_heavy_hitters = heavy_hitters.count()
        total_filtered = total_heavy_hitters
        sort_order = self.get_sort(request)

        if search_param:
            heavy_hitters = heavy_hitters.filter(company__icontains=search_param)
            total_filtered = heavy_hitters.count()

        if sort_order:
            heavy_hitters = heavy_hitters.order_by(*sort_order)

        serializer = self.serializer_class(heavy_hitters[start_num:end_num], many=True)

        return Response(
            {
                "status": "success",
                "draw": draw,
                "recordsTotal": total_heavy_hitters,
                "recordsFiltered": total_filtered,
                "job_applications": serializer.data,
            }
        )

    def post(self, request) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['when'] = date.today()
            serializer.save()
            return Response(
                {
                    "status": "success",
                    "heavy_hitter": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {
                    "status": "fail",
                    "message": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

class HeavyHitterDetail(generics.GenericAPIView):
    serializer_class = HeavyHittersSerializer
    queryset = heavyHitter.objects.all()

    def get_application(self, pk):
        try:
            return heavyHitter.objects.get(pk=pk)
        except Exception:
            return None

    def get(self, request, pk):
        heavy_hitter = self.get_application(pk=pk)
        if heavy_hitter is None:
            return Response(
                {
                    "status": "fail",
                    "message": f"Requests for block: {pk} not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(heavy_hitter)
        return Response(
            {
                "status": "success",
                "heavy_hitter": serializer.data,
            }
        )

    def patch(self, request, pk):
        job_application = self.get_application(pk=pk)
        if job_application is None:
            return Response(
                {
                    "status": "fail",
                    "message": f"H with Id: {pk} not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success",
                    "job_application": serializer.data,
                },
            )
        else:
            return Response(
                {
                    "status": "fail",
                    "message": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        job_application = self.get_application(pk=pk)
        if job_application is None:
            return Response(
                {
                    "status": "fail",
                    "message": f"Job Application with Id: {pk} not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        job_application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
