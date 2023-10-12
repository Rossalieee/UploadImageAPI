import factory
from django.contrib.auth import get_user_model
from ..models import AccountTier

UserModel = get_user_model()


class AccountTierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AccountTier

    name = factory.Faker('user_name')
    allow_expiring_link = False
    allow_original_image = False


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserModel

    username = factory.Faker('user_name')
    _raw_password = 'password'
    password = factory.PostGenerationMethodCall('set_password', _raw_password)
    tier = factory.SubFactory(AccountTierFactory)
