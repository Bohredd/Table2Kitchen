from .views import PedidoViewSet, StatusPedidoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api/pedido", PedidoViewSet)
router.register("api/statuspedido", StatusPedidoViewSet)

urlpatterns = router.urls
