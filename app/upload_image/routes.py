from django.urls import include, path
from rest_framework import routers

from images.views import ImageViewSet, ExpiringLinkViewSet

router_api = routers.SimpleRouter()
router_api.register(r"images", ImageViewSet, basename="images")
router_api.register(r"expiring-links", ExpiringLinkViewSet, basename="expiring-links")

api_urls = [
    path("", include(router_api.urls))]
