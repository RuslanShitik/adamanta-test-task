from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import pre_save

from refunds.models import RefundRequest


@receiver(sender=RefundRequest, signal=pre_save)
def refund_request_pre_save(sender, instance, **kwargs):
    if instance.id:
        old_instance = RefundRequest.objects.get(id=instance.id)
        if old_instance.status != instance.status:
            send_mail(
                subject=f"Refund request #{instance.id} status update",
                message=f"Your refund request #{instance.id} status has been updated from '{old_instance.status}' to '{instance.status}'.",
                from_email=None,
                recipient_list=[instance.user.email],
                fail_silently=True
            )
