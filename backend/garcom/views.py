from rest_framework import viewsets
from .models import Garcom
from .serializers import GarcomSerializer


class GarcomViewSet(viewsets.ModelViewSet):
    queryset = Garcom.objects.all()
    serializer_class = GarcomSerializer