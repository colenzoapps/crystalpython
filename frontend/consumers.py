from django.conf import settings
import asyncio
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class FrontendConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("frontend", self.channel_name)
        print(f"Added {self.channel_name} channel to frontend")

    async def disconnect(self, action):
        await self.channel_layer.group_discard("frontend", self.channel_name)
        print(
            f"Removed {self.channel_name} channel from frontend: Action: {action}")

    async def frontend_gossip(self, event):
        await self.send_json(event)
        print(f"Got message {event} at {self.channel_name}")
