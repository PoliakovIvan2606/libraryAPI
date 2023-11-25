from django.db.models.signals import post_save
from django.dispatch import receiver
from users.tasks import send_welcome_email
from users.models import User

@receiver(post_save, sender=User)
def send_welcome_email_signal(sender, instance, created, **kwargs):
    if created:
        send_welcome_email.delay(instance.email)