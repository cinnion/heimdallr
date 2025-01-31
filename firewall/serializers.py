from rest_framework import serializers
from .models import Blackhole, HeavyHitter


class HeavyHittersSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeavyHitter
        fields = "__all__"

class BlackholeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blackhole
        fields = "__all__"
