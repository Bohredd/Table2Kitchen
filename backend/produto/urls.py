from .views import CategoriaViewSet, ProdutoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api/categoria", CategoriaViewSet)
router.register("api/produto", ProdutoViewSet)

urlpatterns = router.urls
