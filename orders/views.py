from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from orders.models import Cart
from orders.serializers import CartSerializer
from users.permissions import IsProfileOwnerOrAdmin


class CartViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
