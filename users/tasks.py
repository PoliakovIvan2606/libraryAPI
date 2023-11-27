import logging
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

# Создаём задачу celery для отправки сообщения
@shared_task
def send_welcome_email(user_email):
    subject = 'Добро пожаловать!'
    message = 'Спасибо за регистрацию на нашем сайте.'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [user_email]

    send_mail(subject, message, from_email, to_email)