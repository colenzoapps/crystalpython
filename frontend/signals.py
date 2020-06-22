# from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from datetime import datetime
from rest_framework.authtoken.models import Token
from django.conf import settings
from frontend.models import *
# settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=Order)
def save_new_order(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()

    if created:
        async_to_sync(channel_layer.group_send)(
            "frontend", {
                "type": "frontend.gossip",
                "event": "New_Order",
                "id": instance.id,
                "username": instance.lastEditBy,
                "subject": instance.subject,
                "priority": str(instance.priority),
                "status": instance.status
                })
    else:
        async_to_sync(channel_layer.group_send)(
            "frontend", {
                "type": "frontend.gossip",
                "event": "Updated_Order",
                "id": instance.id,
                "username": instance.lastEditBy,
                "subject": instance.subject,
                "priority": str(instance.priority),
                "status": instance.status
                })
