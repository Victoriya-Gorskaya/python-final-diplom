import json

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver, Signal
from django_rest_passwordreset.signals import reset_password_token_created
import os
from .models import ConfirmEmailToken, User
from dotenv import load_dotenv

load_dotenv()
new_user_registered = Signal('user_id')

new_order = Signal('user_id')


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, **kwargs):
    # send an e-mail to the user

    msg = EmailMultiAlternatives(

        f"Password Reset Token for {reset_password_token.user}",
        reset_password_token.key,
        settings.EMAIL_HOST_USER,
        [reset_password_token.user.email]
    )
    msg.send()


@receiver(new_user_registered)
def new_user_registered_signal(user_id, **kwargs):
    # send an e-mail to the user
    token, _ = ConfirmEmailToken.objects.get_or_create(user_id=user_id)

    msg = EmailMultiAlternatives(

        f"Password Reset Token for {token.user.email}",
        token.key,
        settings.EMAIL_HOST_USER,
        [token.user.email]
    )
    if token.user.email == 'test@test.com':
        with open(os.getenv('path_file'), 'w') as s:
            json.dump({'tok': token.key}, s)
    msg.send()


@receiver(new_order)
def new_order_signal(user_id, **kwargs):
    # send an e-mail to the user
    user = User.objects.get(id=user_id)

    msg = EmailMultiAlternatives(

        f"Обновление статуса заказа",
        'Заказ сформирован',
        settings.EMAIL_HOST_USER,
        [user.email]
    )
    msg.send()
