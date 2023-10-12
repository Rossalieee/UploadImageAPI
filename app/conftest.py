import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from images.models import ThumbnailSize
from images.tests.factories import ThumbnailSizeFactory
from users.models import AccountTier
from users.tests.factories import UserFactory, AccountTierFactory

UserModel = get_user_model()


@pytest.fixture(name='basic_thumbnail_size')
def _basic_thumbnail_size() -> ThumbnailSize:
    basic_thumbnail_size = ThumbnailSizeFactory(height=200, width=0)
    return basic_thumbnail_size


@pytest.fixture(name='basic_tier')
def _basic_tier(basic_thumbnail_size) -> AccountTier:
    basic_tier = AccountTierFactory(name='Basic')
    basic_tier.thumbnail_sizes.add(basic_thumbnail_size)
    return basic_tier


@pytest.fixture(name='basic_user')
def _basic_user(basic_tier) -> UserModel:
    user = UserFactory.create(tier=basic_tier)
    return user


@pytest.fixture(name='api_client')
def _api_client(basic_user) -> APIClient:
    client = APIClient()
    client.force_authenticate(user=basic_user)
    return client
