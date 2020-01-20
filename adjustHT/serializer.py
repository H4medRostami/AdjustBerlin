
from rest_framework import serializers


class FilterSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    date = serializers.DateField(required=False)
    channel = serializers.CharField(max_length=20, required=False)
    country = serializers.CharField(max_length=2, required=False)
    os = serializers.CharField(max_length=7, required=False)
    impressions = serializers.IntegerField(required=False)
    clicks = serializers.IntegerField(required=False)
    installs = serializers.IntegerField(required=False)
    spend = serializers.FloatField(required=False)
    revenue = serializers.FloatField(required=False)
    CPI = serializers.FloatField(required=False)


class EntrySerializer(serializers.Serializer):
    date_from = serializers.DateField(required=False)
    date_to = serializers.DateField(required=False)
    channel = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    os = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    group_by = serializers.CharField(required=False)
    sort_by = serializers.CharField(required=False)
