from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from product import views as product_views

router = DefaultRouter()
router.register(r"products", product_views.ProductViewSet, basename="product")
router.register(r"types", product_views.TypeViewSet, basename="type")
router.register(r"prices", product_views.PriceViewSet, basename="price")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
