from rest_framework.routers import DefaultRouter

from orders.views import CartViewSet

router = DefaultRouter()
router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = router.urls
