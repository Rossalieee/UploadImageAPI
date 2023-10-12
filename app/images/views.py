from datetime import datetime, timedelta

from django.http.request import HttpRequest
from django.utils.crypto import get_random_string
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from .models import Image, ExpiringLink
from .permissions import HasExpiringLinkPermission
from .serializers import ExpiringLinkSerializer, ExpiringLinkListSerializer, ImageSerializer, OriginalImageSerializer


class ImageViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    def get_serializer_class(self):
        user = self.request.user
        if user.tier.allow_original_image:
            return OriginalImageSerializer
        return ImageSerializer

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)

    def create(self, request: HttpRequest, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = request.user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class ExpiringLinkViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ExpiringLink.objects.all()
    permission_classes = [HasExpiringLinkPermission]

    def get_serializer_class(self):
        if self.action == 'create':
            return ExpiringLinkSerializer
        return ExpiringLinkListSerializer

    def create(self, request, *args, **kwargs):
        # Generating a unique token for the link
        token = get_random_string(length=32)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        expiration_time = request.data.get('expiration_time')
        expiration_datetime = datetime.now() + timedelta(seconds=int(expiration_time))
        link = f'/download-image/{request.data.get("image")}/image/?token={token}&expiration={expiration_datetime.timestamp()}'

        serializer.validated_data['expiration_datetime'] = expiration_datetime
        serializer.validated_data['link'] = link
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
