from .views import RestauranteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api/restaurante", RestauranteViewSet)

urlpatterns = router.urls
