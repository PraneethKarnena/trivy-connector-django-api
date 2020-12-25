from django.db.models.signals import post_save
from django.dispatch import receiver

from api.models import ScanResult
from api.tasks import scan_target_asynchronously



@receiver(post_save, sender=ScanResult)
def scan_target(sender, instance, created, **kwargs):
    if created:
        scan_target_asynchronously.delay(instance.pk)