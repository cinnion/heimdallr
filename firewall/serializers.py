from rest_framework import serializers
from .models import Blackhole, heavyHitter


class HeavyHittersSerializer(serializers.ModelSerializer):
    class Meta:
        model = heavyHitter
        fields = "__all__"

class BlackholeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blackhole
        fields = "__all__"
