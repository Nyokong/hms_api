import json
from channels.generic.websocket import AsyncWebsocketConsumer

class FeedbackChannel(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.chat_group = 'chat_%s' % self.chat_id

        await self.channel_layer.group_add(
            self.chat_group,
            self.channel_name
        )

        await self.channel_layer.group_send(
            self.chat_group,
            {
                'type':'tester_message',
                'tester':'tester',
            }
        )

    async def tester_message(self, event):
        tester = event['tester']

        await self.send(text_data=json.dumps({
            'tester':tester,
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.chat_group,
            self.channel_name
        )