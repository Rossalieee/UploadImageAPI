from django.db import migrations


def create_default_tiers(apps, schema_editor):
    AccountTier = apps.get_model('users', 'AccountTier')
    ThumbnailSize = apps.get_model('images', 'ThumbnailSize')

    thumbnail_200 = ThumbnailSize.objects.create(height=200, width=0)
    thumbnail_400 = ThumbnailSize.objects.create(height=400, width=0)

    basic_tier = AccountTier.objects.create(
        name='Basic',
        allow_expiring_link=False,
        allow_original_image=False,
    )
    basic_tier.thumbnail_sizes.add(thumbnail_200)

    premium_tier = AccountTier.objects.create(
        name='Premium',
        allow_expiring_link=False,
        allow_original_image=True,
    )
    premium_tier.thumbnail_sizes.add(thumbnail_200)
    premium_tier.thumbnail_sizes.add(thumbnail_400)

    enterprise_tier = AccountTier.objects.create(
        name='Enterprise',
        allow_expiring_link=True,
        allow_original_image=True,
    )
    enterprise_tier.thumbnail_sizes.add(thumbnail_200)
    enterprise_tier.thumbnail_sizes.add(thumbnail_400)


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('images', '0002_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_tiers),
    ]
