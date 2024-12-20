from .views import MesaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api/mesa", MesaViewSet)

urlpatterns = router.urls
