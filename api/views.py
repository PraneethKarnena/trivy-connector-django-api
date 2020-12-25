from rest_framework import generics

from api.serializers import ScanResultSerializer


class ScanView(generics.CreateAPIView):
    serializer_class = ScanResultSerializer
    