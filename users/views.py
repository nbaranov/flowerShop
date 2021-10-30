from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from users.models import Profile
from users.permissions import IsProfileOwnerOrAdmin
from users.serializers import ProfileSerializer


class ProfileViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    queryset = Profile.objects.all()
    permission_classes = (IsProfileOwnerOrAdmin,)
    serializer_class = ProfileSerializer
