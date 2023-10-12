import factory
from django.core.files.uploadedfile import SimpleUploadedFile
from ..models import ThumbnailSize, Image, ExpiringLink
from users.tests.factories import UserFactory


class ThumbnailSizeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ThumbnailSize


class ImageFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Image

    original_file = factory.LazyFunction(
        lambda: SimpleUploadedFile('test.jpg', b'test', 'image/jpeg')
    )
    user = factory.SubFactory(UserFactory)


class ExpiringLinkFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ExpiringLink

