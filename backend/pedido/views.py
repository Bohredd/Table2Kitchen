from rest_framework import viewsets
from .models import Pedido, StatusPedido
from .serializers import PedidoSerializer, StatusPedidoSerializer


class StatusPedidoViewSet(viewsets.ModelViewSet):
    queryset = StatusPedido.objects.all()
    serializer_class = StatusPedidoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer