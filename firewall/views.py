from typing import List, Optional

from django.shortcuts import render
from django.http import HttpResponse
from .models import Blackhole, HeavyHitter

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

    def get(self, request) -> Response:
        draw = int(request.GET.get("draw", 1))
        start_num = int(request.GET.get("start", 1))
        length = int(request.GET.get("length", 10))
        end_num = start_num + length
        search_param = request.GET.get("search[value]")
        blackholes = Blackhole.objects.all()
        total_blackholes = blackholes.count()
        total_filtered = total_blackholes
        sort_order = self.get_sort(request)

        if search_param:
            blackholes = blackholes.filter(cidrBlock__icontains=search_param)
            total_filtered = blackholes.count()

        if sort_order:
            blackholes = blackholes.order_by(*sort_order)

        serializer = self.serializer_class(blackholes[start_num:end_num], many=True)

        return Response(
            {
                "status": "success",
                "draw": draw,
                "recordsTotal": total_blackholes,
                "recordsFiltered": total_filtered,
                "blackholes": serializer.data,
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
    queryset = HeavyHitter.objects.all()

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
        heavy_hitters = HeavyHitter.objects.all()
        total_heavy_hitters = heavy_hitters.count()
        total_filtered = total_heavy_hitters
        sort_order = self.get_sort(request)

        if search_param:
            heavy_hitters = heavy_hitters.filter(cidrBlock__icontains=search_param)
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
                "heavy_hitters": serializer.data,
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
    queryset = HeavyHitter.objects.all()

    def get_heavy_hitter(self, pk):
        try:
            return HeavyHitter.objects.get(pk=pk)
        except Exception:
            return None

    def get(self, request, pk):
        heavy_hitter = self.get_heavy_hitter(pk=pk)
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
        heavy_hitter = self.get_heavy_hitter(pk=pk)
        if heavy_hitter is None:
            return Response(
                {
                    "status": "fail",
                    "message": f"Heavy hitter with Id: {pk} not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success",
                    "heavy_hitter": serializer.data,
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
        heavy_hitter = self.get_heavy_hitter(pk=pk)
        if heavy_hitter is None:
            return Response(
                {
                    "status": "fail",
                    "message": f"Heavy Hitter with Id: {pk} not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        heavy_hitter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
