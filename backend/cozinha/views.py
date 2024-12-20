from rest_framework import viewsets
from .models import Restaurante
from .serializers import RestauranteSerializer

class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

    