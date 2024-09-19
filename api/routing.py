from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/feedback/', consumers.FeedbackChannel.as_asgi()),
    # re_path(r'ws/test/(?P<chat_id>\w+)/$', channels.TestChannel),
]