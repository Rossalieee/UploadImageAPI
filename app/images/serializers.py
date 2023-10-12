from easy_thumbnails.files import get_thumbnailer
from rest_framework import serializers

from .models import Image, ExpiringLink


class OriginalImageSerializer(serializers.ModelSerializer):
    thumbnails = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['thumbnails', 'original_file']
        read_only_fields = ['thumbnails']

    def get_thumbnails(self, obj: Image):
        user = self.context['request'].user
        thumbnail_sizes = user.tier.thumbnail_sizes.all()
        all_thumbnails = {}

        for size in thumbnail_sizes:
            options = {'size': (size.height, size.width), 'crop': True}
            thumbnailer = get_thumbnailer(obj.original_file)
            thumbnail = thumbnailer.get_thumbnail(options)
            all_thumbnails[f'thumbnail_{size.height}x{size.width}'] = thumbnail.url

        return all_thumbnails


class ImageSerializer(OriginalImageSerializer):
    class Meta(OriginalImageSerializer.Meta):
        extra_kwargs = {
            'original_file': {'write_only': True}
        }


class ExpiringLinkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpiringLink
        fields = ['image', 'link']


class ExpiringLinkSerializer(ExpiringLinkListSerializer):
    class Meta(ExpiringLinkListSerializer.Meta):
        fields = ExpiringLinkListSerializer.Meta.fields + ['expiration_time']
        read_only_fields = ['link']
