from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from app_svelte_van_itten.consumers import ChatConsumer
application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/uzenetek/', ChatConsumer.as_asgi()),
    ])
})