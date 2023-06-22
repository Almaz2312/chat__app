import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from chat.models import Message, Group


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]

        if self.user.is_anonymous:
            await self.close()

        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        await database_sync_to_async(self._create_group)(name=self.room_group_name)

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        print("CHECK text_data HERE!!!", text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        print("CHECK event HERE!!!", event)
        message = event["message"]

        # Create message object
        await database_sync_to_async(self._create_message)(send_by=self.user.id)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))

    def _create_message(self, **kwargs) -> Message:
        return Message.objects.create(**kwargs)

    def _create_group(self, **kwargs) -> Group:
        group, _ = Group.objects.get_or_create(**kwargs)
        return group
