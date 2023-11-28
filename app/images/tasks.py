from celery import shared_task
from django.utils import timezone
from .models import ExpiringLink


@shared_task
def delete_expired_links():
    current_time = timezone.now()

    # Find all expired links in the database
    expired_links = ExpiringLink.objects.filter(expiration_datetime__lt=current_time)

    # Delete all expired links
    for link in expired_links:
        link.delete()
