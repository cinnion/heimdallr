from rest_framework import serializers
from .models import heavyHitter


class HeavyHittersSerializer(serializers.ModelSerializer):
    class Meta:
        model = heavyHitter
        fields = "__all__"
