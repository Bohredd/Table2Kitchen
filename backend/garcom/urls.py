from .views import GarcomViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api/garcom", GarcomViewSet)

urlpatterns = router.urls
