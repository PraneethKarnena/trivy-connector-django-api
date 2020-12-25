from rest_framework import generics

from api.serializers import ScanResultSerializer
from api.models import ScanResult


class ScanView(generics.CreateAPIView):
    serializer_class = ScanResultSerializer


class ScanResultView(generics.RetrieveAPIView):
    queryset = ScanResult.objects.all()
    serializer_class = ScanResultSerializer
    