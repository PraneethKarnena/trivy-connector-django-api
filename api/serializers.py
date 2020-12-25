from rest_framework import serializers

from api.models import ScanResult


class ScanResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScanResult
        fields = '__all__'
        read_only_fields = ['result', 'status', 'has_error', 'error_message']